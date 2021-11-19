from sys import platform
from os import system
from random import randint

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
    return platform

def clearCMD():
    system('"clear"')

def random3D6():
    result = 0
    for i in range(3):
        result += randint(1, 6) # This gives a nice bell curve
    return result
