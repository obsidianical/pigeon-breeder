import sys
import os

"""
Shared Functions
"""
def isNotEmpty(List):
    return bool(len(List))

def isEmpty(List):
    return not isNotEmpty(List)

def inputString():
    return "\nWhat do you do? "

def whatOS():
    return sys.platform

def clearCMD():
    os.system('"clear"')
