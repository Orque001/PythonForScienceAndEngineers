#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Reader file that reads a given file and creates a graph
Inputs: loads data files
Outputs: displays a graph of the given data
Dependencies: import time module, import os module, numpy as py module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1
@author: rielorque
"""
# Import all of your modules needed for this project.
import time
import matplotlib.pyplot as plt
import numpy as np

# Load data from files
def loadData(filename):
    """
    loadData function to load data from a given file
    Inputs: takes in the filename of the file
    Outputs: no outputs
    Usage: used to load data and return the value x and y
    """
    # Load data from file
    x, y = np.loadtxt(filename)
    return x, y

# Write a function Plot data.
def plotData(x1, y1, x2, y2):
    """
    plotData to plot data of the given files
    Inputs: takes in arguements x1, x2, y1, y2
    Outputs: displays a graph with a legend
    Usage: used to create a graph and display data
    """
    # Plot data
    plt.plot(x2, y2, label="Cos")
    plt.plot(x1, y1, label="Sinc")
    
    plt.xlabel("X Data")
    plt.ylabel("Y Data")
    plt.title("Two variable plot containing 101 samples")
    plt.legend()

    plt.savefig("Riel_Orque_project_6.jpg")

    plt.show()


def main():
    """
    Main function is the starting point of execution
    Inputs: No user inputs
    Outputs: Displays name, current time, and displays a graph
    Usage: Starting point of execution
    """
    # displays name and current time
    print("\nRiel", time.asctime())
    
    # Load data from files
    x_sinc, y_sinc = loadData("Riel_Orque_sinc.txt")
    x_cos, y_cos = loadData("Riel_Orque_cos.txt")

    # Call plot function to chart the data
    plotData(x_sinc, y_sinc, x_cos, y_cos)


if __name__ == "__main__":
    main()
