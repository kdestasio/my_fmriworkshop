#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:54:27 2017

@author: kristadestasio
"""
import glob
import os
import shutil
import pdb
import pandas
import argparse

#def prepro(basedir):
#    print('Hello data is in the path '+basedir)    
    
#def main():
    # Will run global variables and prepro
#    basedir='/Users/kristadestasio/Desktop/data'
#    prepro(basedir)
    
#main() # call main to execut all our globals then run our prepro function

input=glob.glob('/Users/kristadestasio/Desktop/data/sub-*/func/sub-*bart*.nii.gz') # Matlab also has the glob function
print(input[0:10])

len(input)

# Separate the part of the path that is the subject information
x=input[0]
print('my path is ' +x)
y=x.split('/')
print (y)
sub=y[7]
print(sub)

# Separate out the task name
subtask=input[1].split('/')[7].split('.')[0]
print(subtask)

# Name the files by appending "_brain"
output=subtask+'_brain'
print(output)

# Create a variable with wildcard characters
basedir='/Users/kristadestasio/Desktop/data'
path=os.path.join(basedir, 'sub-*', 'func', 'sub-*bart*.nii.gz')
print(path)
input=glob.glob(path)
len(input[1:5])
print(input[0:2])

# For loop to iterate through and bet
def prepro(basedir):
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')):
        input=item
        output_path=item.strip('.nii.gz')
        output=output_path+('_brain')
        os.system("/usr/local/fsl/bin/bet %s %s -F"%(input, output))
#        pdb.set_trace() # debug
def main():
    basedir='/Users/kristadestasio/Desktop/data'
    prepro(basedir)
main()

