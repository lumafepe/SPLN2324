#!/usr/bin/env python3

'''
Name 

SYNOPSIS


DESCRIPTIONS

FILES:


'''

__version__ = "0.0.1"

import os
import sys
from .templates import get_pyproject,prependPythonData
from jjcli import *
import json
import shutil
    



def create_project_structure(name):
    # Create main folder
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Directory already exists.")

    # Create subfolders
    os.makedirs(os.path.join(name, 'tests'))
    os.makedirs(os.path.join(name, name))

def moveItems(foldername):
    files_and_folders = os.listdir('.')
    for item in files_and_folders:
        if item != foldername:
            try:
                shutil.move(item, os.path.join(foldername,foldername, item))
            except Exception as e:
                print(f"Failed to move '{item}' to '{foldername}/{foldername}' directory. Error: {e}")

def flagOrInput(flag,cl,text):
    if "-"+flag in cl.opt:
        return cl.opt.get("-"+flag)
    else:
        return input(text+": ")

def getUserMetadata(cl):
    username = None
    email = None
    metafile = os.path.join(os.path.expanduser("~/.METADATA.json"))
    if os.path.isfile(metafile):
        with open(metafile) as f:
            data = json.load(f)
            username = data.get("Username",None)
            email = data.get("Email",None)
    if username == None:
        username = flagOrInput("u",cl,"username")
    if email == None:
        email = flagOrInput("e",cl,"email")
        
    return username,email


def main():
    project_name = None
    command_name = None
    file_main = None
    cl = clfilter("n:c:f:u:e:", doc=__doc__) ## Option values in cl.opt dictionary
    project_name = flagOrInput("n",cl,"project name")
    command_name = flagOrInput("c",cl,"command name")
    file_main = flagOrInput("f",cl,"main file")
    if not (os.path.isfile(file_main)):
        print(f"file {file_main} not found")
        exit()
    
    pathTofolder = os.path.abspath(project_name)
    pathToSrc = os.path.join(pathTofolder,project_name)
    username,email = getUserMetadata(cl)
    
    create_project_structure(project_name)
    moveItems(project_name)
    
    with open(os.path.join(pathTofolder,"pyproject.toml"),"w") as f:
        f.write(get_pyproject(project_name,command_name,username,email))
    with open(os.path.join(pathTofolder,'README.md'), 'w') as f:
        pass
    try:
        shutil.move(os.path.join(pathToSrc, file_main), os.path.join(pathToSrc, "__init__.py"))
    except Exception as e:
        print(f"Failed to rename '{file_main}' to '__init__.py'. Error: {e}")
    prependPythonData(os.path.join(pathToSrc, "__init__.py"))
    