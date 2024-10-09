#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Write a Python program that generates white and Gaussian noise,
    plots a sampling of each type of noise using a line plot (2 plots), 
    computes and plots a histogram of each sampling using a bar chart (2 plots), 
    and uses matplotlib's subplots capability to lay out all four plots into a 
    single figure, which includes an overall title.
Inputs: No user input
Outputs: displays a graph of the noise samples and distributions
Dependencies: import time module, import matplotlib module, numpy as py module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1
@author: rielorque
"""
# Import all of your modules needed for this project.
import time
import matplotlib.pyplot as plt
import numpy as np

# Write a function to generate white noise
def generate_white_noise(num_samples, min_val = -1.0, max_val = 1.0):
    """ 
    Generate white noise and return a NumPy array.
    Inputs: num_samples, min_val, max_val
    Outputs: No outputs
    Returns: an array generated white noise
    Usage: Generate white noise and return an array
    """
    return np.random.uniform(min_val, max_val, num_samples)

# Write a function to generate gaussian noise
def generate_gaussian_noise(num_samples, mu = 0.0, sigma = 0.34):
    """
    Generate Gaussian noise and return a NumPy array.
    Inputs: num_samples, mu, sigma
    Outputs: No outputs
    Returns: an array generated gaussian noise
    Usage: Generate gaussian noise and return an array
    """
    return np.random.normal(mu, sigma, num_samples)

# Write a function to Plot your figure / chart for this project
def plot_data(white_noise, gaussian_noise):
    """
    Plot a 2x2 figure with line plots and histograms for white and Gaussian noise
    Inputs: white_noise, gaussian_noise
    Outputs: No outputs
    Returns: an array generated gaussian noise
    Usage: Generate gaussian noise and return an array
    """
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Noise Samples and Distributions (N=1001)', fontsize=16)

    # White noise line plot
    axs[0, 0].plot(white_noise)
    axs[0, 0].set_title('White Noise, min = 0.0, max = 1.0')

    # White noise histogram
    axs[0, 1].hist(white_noise, rwidth=0.8)
    axs[0, 1].set_title('White Noise Histogram')

    # Gaussian noise line plot
    axs[1, 0].plot(gaussian_noise)
    axs[1, 0].set_title('Gaussian Noise, μ = 0.5, σ = 0.125')

    # Gaussian noise histogram
    axs[1, 1].hist(gaussian_noise, rwidth=0.8)
    axs[1, 1].set_title('Gaussian Noise Histogram')

    plt.savefig("Riel_Orque_project_07.png")
    plt.show()

# Write a main function
def main():
    """
    Main function is the starting point of execution
    Inputs: No user inputs
    Outputs: Displays name, current time, and displays a graph
    Usage: Starting point of execution
    """
    # displays name and current time
    print("\nRiel", time.asctime())

    # Set your hard code values
    num_samples = 1001
    minimum = 0.0
    maximum = 1.0
    mu = 0.5
    sigma = 0.125

    # Call the white noise function
    white_noise = generate_white_noise(num_samples, minimum, maximum)
    
    # Call the gaussian noise function
    gaussian_noise = generate_gaussian_noise(num_samples, mu, sigma)

    # Call your Plot figure function
    plot_data(white_noise, gaussian_noise)

# Only Global / top code in your program.
if __name__ == "__main__":
    main()
