#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Riel Orque
Created on Thu Nov  9 16:47:25 2023
CSC 309 SFSU Spring 2023
Project 8 due 11/10/2023 23:59 PST

Description: 
    Use numpy.linspace to generate a sampling from -2pi to 2pi over 101 steps, and then to use numpy array operations to compute a new array containing y = cos( x ).
    Use your project #7 function that generates white noise. Generate white noise in the range 0 .. 1, then scale the noise to be S = 0.1, or 10%, of the magnitude of the range of the function y = cos( x ).
    Use NumPy array methods to add this noisy signal to your clean signal (hint: this is one line of code). 
    Use matplotlib.pyplot to make a 2-variable line chart showing the clean signal, y = cos( x ), and the noisy signal.
Outputs: no outputs
Dependencies: import time module, import matplotlib module, numpy as py module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1
@author: rielorque
"""
# Import all of your modules needed for this project.
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Function to generate white noise
def create_noise(size):
    """
    Creates noise using numpy
    Inputs: size
    Outputs: No outputs
    Returns: returns a random size
    Usage: create random noise
    """
    return 0.1 * np.random.rand(size)

# Function to save data to a file
def save_data(x, clean_signal, noisy_signal, filename):
    """
    Saves data into a txt file
    Inputs: white_noise, gaussian_noise
    Outputs: No outputs
    Returns: an array generated gaussian noise
    Usage: Generate gaussian noise and return an array
    """
    header = f"Author: Riel Orque\nDate: {datetime.date.today()}\nDescription: Data file for clean and noisy signals."
    np.savetxt(filename, np.column_stack((x, clean_signal, noisy_signal)), header=header, comments="", fmt='%.6f', delimiter=' ')

# Write a main function
def main():
    """
    Main function
    Inputs: no inputs
    Outputs: no outputs
    Returns: no returns
    Usage: Generate gaussian noise and return an array
    """
    # Generate x values from -2pi to 2pi
    x = np.linspace(-2 * np.pi, 2 * np.pi, 101)

    # signal y = cos(x)
    signal = np.cos(x)

    # Generate noise and add to signal
    noise = create_noise(len(x))
    noisy_signal = signal + noise
    
    # call save_data to save as txt file
    save_data(x, signal, noisy_signal, 'RielOrque_project_8.txt')


if __name__ == "__main__":
    main()
