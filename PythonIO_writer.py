#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Writer file to create data and save
Inputs: No user inputs
Outputs: No user outputs
Dependencies: import time module, import os module, numpy as py module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1
@author: rielorque
"""
# Import all of your modules needed for this project.
import time
import numpy as np

# Write a function to save data to a file. This function has has 4 arguments: xvals, yvals, filename, header comment. 
def saveData(xvals, yvals, filename, header_comment1, header_comment2):
    """
    saveData function that saves the data and takes in 5 arguments
    Inputs: 5 arguments of xvals, yvals, filename, header_comment1, header_comment2
    Outputs: No output
    Usage: used to save data
    """
    # Create header containing name, date, and description
    header = f"# Author: Riel Orque Date: {header_comment1}\n# Description: {header_comment2}\n"
    
    # Save data to file
    np.savetxt(filename, (xvals, yvals), header=header, fmt='%10.4f', comments='')

# Write a main function
def main():
    """
    Main function is the starting point of execution
    Inputs: Variables x, y1, y2 to create data and use numpy
    Outputs: Displays name, current time, and creates data
    Usage: Starting point of execution
    """
    # displays name and current time
    print("\nRiel", time.asctime())
    
    # Create data: x, y1, y2
    x = np.linspace(-2 * np.pi, 2 * np.pi, 101)
    y1 = np.sinc(x)
    y2 = np.cos(x)

    # Call save data function to Save file 1
    saveData(x, y1, "Riel_Orque_sinc.txt", time.asctime(), "A list of sinc function values")

    # Call save data function to Save file 2
    saveData(x, y2, "Riel_Orque_cos.txt", time.asctime(), "A list of cosine function values")
    
# Only Global / top code in your program.
if __name__ == "__main__":
    main()
    
    
    
