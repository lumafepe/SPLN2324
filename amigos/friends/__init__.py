#!/usr/bin/env python3

'''
Name 
    friends - Calculates friends in a text

SYNOPSIS
    friends [options] input_files
    option: 
        -m <+|-> - Sort increasing or decreasing
        -n - Order alfabetically
        -l <n> limit to n results
        

DESCRIPTIONS

FILES:


'''

from collections import Counter
from jjcli import *
import re
import os
from .friends import get_subject_predicate_relations

__version__ = "0.0.1"


def printWordsList(list):
    for (p1,p2), occ in list:
        print(f"{p1} e {p2} são amigos {occ} vezes.")
        
    
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
    


        

def main():
    cl = clfilter("l:m:n", doc=__doc__) ## Option values in cl.opt dictionary

    for txt in cl.text():
        if "-n" in cl.opt and "-m" in cl.opt:
            print("FLAGS INCOMPATIVEIS")
            exit()
            
        count = get_subject_predicate_relations(txt)
        dic = list(count.items())
        
        if "-n" in cl.opt:
            dic.sort(key=lambda x:x[0])
   
        if "-m" in cl.opt:
            dic.sort(key=lambda x:x[1],reverse=cl.opt.get("-m")=='-')

        if "-l" in cl.opt:
            dic = dic[:int(cl.opt.get("-l"))]
        printWordsList(dic)
