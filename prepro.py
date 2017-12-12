#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:27 2017

@author: kristadestasio
"""
import glob
import os
import shutil

def prepro(basedir):
    print('Hello data is in the path '+basedir)    
    
def main():
    # Will run global variables and prepro
    basedir='/Users/kristadestasio/Desktop/data'
    prepro(basedir)
    
main() # call main to execut all our globals then run our prepro function