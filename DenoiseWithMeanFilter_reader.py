#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Riel Orque
Created on Thu Nov  9 16:53:13 2023
CSC 309 SFSU Spring 2023
Project 8 due 11/10/2023 23:59 PST

Description: 
    Write a smoothing function that implements a sliding window mean filter over an input array.
    Compute the Mean Square ErrorLinks to an external site. (MSE) of (1) the clean and noisy signals, and (2) the clean and denoised signals. 
    Use matplotlib.pyplot() to create a 3 variable plot showing (1) the clean signal, (2) the noisy signal, and (3) the denoised signal.
Inputs: No user input
Outputs: displays a graph of the noise samples and distributions
Dependencies: import time module, import matplotlib module, numpy as py module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1
@author: rielorque
@author: rielorque
"""
# Import all of your modules needed for this project.
import numpy as np
import matplotlib.pyplot as plt

def smoothing_function(signal, width=5):
    """
    Write a smoothing function that implements a sliding window mean filter over an input array. 
    Inputs: 
    Outputs: No outputs
    Returns: an array generated gaussian noise
    Usage: Generate gaussian noise and return an array
    """
    filtered_signal = np.convolve(signal, np.ones(width)/width, mode='same')
    return filtered_signal 

def mean_square_error(signal1, signal2):
    """
    Compute the Mean Square Error
    Inputs: No inputs
    Outputs: No outputs
    Returns: returns and mean square of given inputs
    Usage: Compute mean square error
    """
    return np.mean((signal1 - signal2) ** 2)

def plot_data(x, clean_signal, noisy_signal, filter_width = 7):
    """
    Use matplotlib.pyplot() to create a 3 variable plot showing (1) the clean signal, (2) the noisy signal, and (3) the denoised signal. 
    Inputs: x, clean_signal, noisy_signal, and filter width
    Outputs: No outputs
    Returns: No returns
    Usage: Plot and display data
    """
    # denoise_signal variable to call smoothing function
    denoised_signal = smoothing_function(noisy_signal, filter_width)

    # mse variables to call mean square error function
    mse_noisy = mean_square_error(clean_signal, noisy_signal)
    mse_denoised = mean_square_error(clean_signal, denoised_signal)

    plt.plot(x, clean_signal, label='y = cos(x), n = 101', color='black', linewidth=.9)
    plt.plot(x, noisy_signal, label=f'noisy signal, mse = {mse_noisy:.4f}', color='red', linewidth=.9)
    plt.plot(x, denoised_signal, label=f'mean filter, w = 7, mse = {mse_denoised:.4f}')
    plt.legend()
    plt.title('Denoising with a Mean Filter')
    plt.savefig("Riel_Orque_project_8.png")
    plt.show()


# Write a main function
def main():
    """
    Main function
    Inputs: 
    Outputs: No outputs
    Returns: an array generated gaussian noise
    Usage: Generate gaussian noise and return an array
    """
    # load txt data
    data = np.loadtxt('RielOrque_project_8.txt', skiprows=3)

    # extract data to the given variables
    x = data[:, 0]
    clean_signal = data[:, 1]
    noisy_signal = data[:, 2]

    # call plot data to plot and display graph
    plot_data(x, clean_signal, noisy_signal, filter_width=7)

# Only Global / top code in your program.
if __name__ == "__main__":
    main()
