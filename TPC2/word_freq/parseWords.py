#!/usr/bin/env python3
import json
import pickle
import re

def main():
    total =0
    data={}
    pattern = re.compile(r'(\w[\w\-]*\w|\w)\t(\d+).*')
    try:
        while True:
            line = input()
            match = pattern.match(line)
            if match:
                data[match.groups()[0]]=int(match.groups()[1])
                total+=int(match.groups()[1])
    except EOFError:
        for k in data.keys():
            data[k] = (1000000 * data[k]) / total
            print(f"{k}   {data[k]}")
            

if __name__ == "__main__":
    main()