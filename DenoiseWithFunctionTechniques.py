#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Riel Orque
Created on Fri Nov 10 20:48:23 2023
CSC 309 SFSU Spring 2023
Project 9 due 12/9/2023 23:59 PST

Description: Write a Python program that performs mean filtering on a noisy signal using Functional Programming techniques.
Outputs: Displays a graph
Dependencies: import time module, import matplotlib module, numpy as py module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1
@author: rielorque
"""

import numpy as np
import matplotlib.pyplot as plt
import datetime

def create_noise(size):
    """
    Function to generate white noise
    Inputs: No user inputs
    Outputs: returns random  white noise
    Usage: Creates white noise
    """
    return 0.1 * np.random.rand(size)

def create_gaussian_noise(size):
    """
    Function to generate Gaussian noise
    Inputs: No user inputs
    Outputs: returns random gaussian noise
    Usage: Creates gaussian noise
    """
    return 0.1 * np.random.randn(size)

def save_data(x, clean_signal, noisy_signal, filename):
    """
    Function to save data to a file
    Inputs: No user inputs
    Outputs: No outputs
    Usage: Used to save data
    """
    header = f"Author: Your Name\nDate: {datetime.date.today()}\nDescription: Data file for clean, noisy, and smoothed signals."
    np.savetxt(filename, np.column_stack((x, clean_signal, noisy_signal)), header=header, comments="", fmt='%.6f', delimiter=' ')

def my_stencil(samples):
    """
    Function to perform sliding window mean filter stencil computation
    Inputs: No user inputs
    Outputs: returns mean
    Usage: Used to perform sliding window mean filter stencil computation
    """
    return np.mean(samples)

def mean_filter(signal, filter_width):
    """
    Function to perform mean filtering using map() operator
    Inputs: No user inputs
    Outputs: returns smoothed_signal
    Usage: Used to perform mean filturing using map() operator
    """
    padded_signal = np.pad(signal, (filter_width // 2, filter_width // 2), mode='wrap')
    smoothed_signal = np.array(list(map(my_stencil, (padded_signal[i:i+filter_width] for i in range(len(signal))))))
    return smoothed_signal

def compute_mse(signal1, signal2):
    """
    Function to compute Mean Square Error (MSE)
    Inputs: No user inputs
    Outputs: returns mean of signal parameters
    Usage: Used to compute MSE
    """
    return np.mean((signal1 - signal2)**2)

def plot_signals(x, clean_signal, noisy_signal, smoothed_w3, smoothed_w7):
    """
    Function to plot the signals
    Inputs: No user inputs
    Outputs:No Outputs
    Usage: Used to generate and display a graph
    """
    plt.plot(x, clean_signal, label='Clean Signal')
    plt.plot(x, noisy_signal, label='Noisy Signal')
    plt.plot(x, smoothed_w3, label='Smoothed (w=3)')
    plt.plot(x, smoothed_w7, label='Smoothed (w=7)')
    plt.legend()
    plt.title('Clean, Noisy, and Smoothed Signals')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
    
    # Save data to a file
    save_data(x, clean_signal, noisy_signal, 'RielOrque_project_9.txt')

# Main function
def main():
    """
    Main function is the starting point of execution
    Inputs: No user inputs
    Outputs: Displays name, current time, and displays a graph
    Usage: Starting point of execution
    """
    # Samples x = -2pi .. 2pi over N = 1001 steps
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1001)

    # Generates a "clean" signal y = sin( x )
    clean_signal = np.sin(x)

    # Generates noise, either white noise or Gaussian noise,
    noise = create_gaussian_noise(len(x))

    # Create noisy signal by adding noise to the clean signal
    noisy_signal = clean_signal + noise

    # Perform mean filtering using map() with filter width w=3
    smoothed_w3 = mean_filter(noisy_signal, filter_width=3)

    # Perform mean filtering using map() with filter width w=7
    smoothed_w7 = mean_filter(noisy_signal, filter_width=7)

    # Compute MSE for signal pairs
    mse_clean_noisy = compute_mse(clean_signal, noisy_signal)
    mse_clean_smoothed_w3 = compute_mse(clean_signal, smoothed_w3)
    mse_clean_smoothed_w7 = compute_mse(clean_signal, smoothed_w7)

    # Print MSE values
    print(f'MSE (Clean-Noisy): {mse_clean_noisy:.4f}')
    print(f'MSE (Clean-Smoothed w3): {mse_clean_smoothed_w3:.4f}')
    print(f'MSE (Clean-Smoothed w7): {mse_clean_smoothed_w7:.4f}')

    # Plot the signals
    plot_signals(x, clean_signal, noisy_signal, smoothed_w3, smoothed_w7)

if __name__ == "__main__":
    main()