#!/usr/bin/env python3

'''
Name 
    WordOccur - Calculates words Occurenceis in a text

SYNOPSIS
    WordOccur [options] input_files
    option: 
        -m 20 - Show the 20 most common
        -n: Order alfabetically
        -i: Ignore case sensitivity
        -l: Language (select language code) 
        -c: 

DESCRIPTIONS

FILES:


'''

from collections import Counter
from jjcli import *
import re
import os

__version__ = "0.0.1"

def tokeniza(text):
    palavras = re.findall(r'\w+(?:\-\w+)?|[,;.:?!_—]+', text)
    # ?: agrupa regex, mas não são tratadas como grupo de captura
    return palavras

def printWordsList(list):
    for word, numb in list:
        print(f"{numb}  {word}")
        
    
def values_dict(c:Counter,flag=False):
    #returns the expected number of times each word appears
    total = c.total()
    print(total)
    with open(os.path.join(os.path.split(__file__)[0],"out.txt")) as f:
        stdvals={}
        for line in f:
            line=line.strip()
            value,expectedPerM = line.split("   ")
            if flag:
                value=value.lower()
            if c[value]!=0:
                stdvals[value]=(total*float(expectedPerM)) / 1000000
    return stdvals
    


def compara_counters(c:Counter,flag=False):
    expect = Counter(values_dict(c,flag))
    d=dict()
    pattern = re.compile(r'\w')
    for item in c:
        if re.search(pattern,item):
            if expect[item]!=0:
                d[item] = ((c[item]-expect[item])/expect[item])*100
            else:
                d[item] = ((c[item]-0.0397)/0.0397)*100 #TODO::FIX
    return Counter(d)
        

def main():
    cl = clfilter("nm:ic", doc=__doc__) ## Option values in cl.opt dictionary

    for txt in cl.text():             ## Process one file at time
        wordsList = tokeniza(txt)
        if "-n" in cl.opt:
            wordsList.sort()
        flag = False
        if "-i" in cl.opt:
            wordsList = [palavra.lower() for palavra in wordsList]
            flag=True
        c = Counter(wordsList)
        if "-c" in cl.opt:
            c = compara_counters(c,flag)
        if "-m" in cl.opt:
            printWordsList(c.most_common(int(cl.opt.get("-m"))))
        else:
            printWordsList(c.items())


# chmod 755 filename, transforma o código num script



"""
arranjar uma tabela padrão de occurencias
buscar apenas 500k (maybe)
numeros serem removidos ( maybe) (tudo com numeros por exemplo 12h53m)
tabela em frequencias relativas
fazer uma função q seja capaz de comparar racios 10000,10020 40,20

"""