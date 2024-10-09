#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: You are going to measure the time your sort function takes to sort a range of values.
Inputs: variable N as the problem size, random seed to generate random numbers
Outputs: Outputs data into a graph
Dependencies: import time module, import random module, matplotlib pyplot module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1

@author: rielorque
"""
import time, random
import matplotlib.pyplot as plt

def iSort(aList):
    """ This function will sort a list
        Inputs: a list of numbers, aList
        Output: returns True if list is sorted, false if not sorted
        Returns: print statement, status
        Usage: Sort a list
    """
    for i in range(1, len(aList)):
        candidate = aList[i]
        j = i - 1
        
        while(j >= 0 and aList[j] > candidate):
            aList[j + 1] = aList[j]
            j -= 1
        aList[j + 1] = candidate

def checkSort(aList):
    """ This function will check if the list is sorted or not
        Inputs: a list of numbers, aList
        Output: returns True if list is sorted, false if not sorted
        Returns: print statement, status
        Usage: Check if list is sorted
    """
    # status variable true
    status = True
    # i variable = to 0
    i = 0
    
    # while loop to loop through the lenght of the list
    while(i < (len(aList) - 1) and status):
        # if list is greater than the list index + 1, set status to true and break
        if(aList[i] > aList[i + 1]):
            status = False
            break
        i = i + 1
        
    # returns print statment and status
    return print("Is this list sorted?  ", status)

def PlotData(problemSize, time):
    """
    PlotData function that plots takes in an x and y data, title, and an x and y axis title hen displays a graph
    Inputs: takes in x an y data input, a titleString, and a label for x and y axis
    Outputs: displays a graph that displays the title, x and y, and plots the graph
    Returns: None
    Usage: Plots data and displays a graph
    """
    plt.figure()
    
    plt.title("Insertion Sort Elapsed Time")
    plt.xlabel("Problem Size")
    plt.ylabel("Time (sec)")
    
    plt.plot(problemSize, time)
    
    plt.savefig("Project_04.jpg", dpi = 600)
    plt.show()

def main():
    """
    Main function is the starting point of execution
    Inputs: 
        variable N with a list of problem size
        random.seed() to initialize random number generator
    Outputs: Displays name and current time
    Usage: Starting point of execution
    """
    # displays name and current time
    print("\nRiel", time.asctime())
    
    # problem sizes
    N = (128, 256, 512, 1024, 2048, 4096, 8192, 16384)
    
    # list of times
    times = []
    
    # for loop to loop through N problem size
    for i in N:
        # random seed to generate random numbers
        random.seed(55)
        
        # lists of random numbers for range i(problem size)
        L1 = [random.randint(0, 9999) for j in range(i)]
        
        print("\nWorking on problem size N = ", i)
        
        
        # call checksort to see if list is sorted
        checkSort(L1)
        
        print("Sorting...")
        
        # start timer to time the iSort function
        start_time = time.time()
        
        # call iSort to sort list
        iSort(L1)
        
        # end timer
        end_time = time.time()
                
        # get the timer in seconds
        elapsed_time = end_time - start_time
        
        # add elapsed time into times list 
        times.append(elapsed_time)
        
        
        # checkSort if list is sorted
        checkSort(L1)
        
        print("Sort time (sec): ", elapsed_time)
    
    # call PlotData() to plot the data and display a graph
    PlotData(N, times)

# calls main() function
if __name__ == "__main__":
    main()

