#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inputs: name
Outputs: Users name and current time
Description: Introduction to python
Dependencies: time
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1

@author: rielorque
"""

import time

#print my name and the current time using asctime() method
print("Riel", time.asctime())

#Prompts user for their name and displays
name = input("What is your name? ")
print(name, time.asctime())
