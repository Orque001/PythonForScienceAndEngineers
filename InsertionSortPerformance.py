#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: Insertion sort performance with python list comprehension and numpy
Dependencies: import time module, import random module, matplotlib.pyplot module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1

@author: rielorque
"""
# Import all of your modules needed for this project.
import time, math, random, array
import matplotlib.pyplot as plt
import numpy as np

# Write a function check_sort to check if the list passed in is in Ascending order. See Project 3 for details.
def CheckSort(aList):
    """ This function will check if the list is sorted or not
        Inputs: a list of numbers, aList
        Output: returns True if list is sorted, false if not sorted
        Returns: print statement, status
        Usage:
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
    # return print("\nIs this list sorted? ", status) 

# Write a function to sort a list of numbers, see Project 4 for details.
def iSort(aList):
    """ This function will sort a list using insertion sort
        Inputs: a list of numbers, aList
        Output: returns True if list is sorted, false if not sorted
        Returns: no returns
        Usage: Sort a list
    """
    for i in range(1, len(aList)):
        candidate = aList[i]
        j = i - 1
        
        while(j >= 0 and aList[j] > candidate):
            aList[j + 1] = aList[j]
            j -= 1
        aList[j + 1] = candidate

# Write a function for Python Lists. It will have the following arguments (1) the set of problem sizes N, (2) your random number seed, (3) your random number minimum value (rand_min), and (4) your random number maximum value (rand_max). 
def PythonList(problem_size, random_seed, rand_min, rand_max):
    """
    PythonList function that creates a python list using list comprehension and times sorting the list
    Inputs: takes arguments of problem_size, random_seed, rand_min, rand_max
    Outputs: returns the list of times in timingList list
    Usage: a function that creates python lists
    """
    # List for time
    timingList = []
    
    # For each problem size:
    for n in problem_size:
        print("doListProblems, doing problem size = ", n)
        
        random.seed(random_seed)
        
        #   Create random list of numbers for current problem size.
        listL = [random.randint(rand_min, rand_max) for i in range(n)]
      
        #   Call Check sort function and print return status
        CheckSort(listL)
      
        #   Start timer
        t1 = time.monotonic()

        #   Call your sort function on current list.
        iSort(listL)

        #   End timer
        t2 = time.monotonic()

        #   Save time
        timingList.append(t2 - t1)

        #   Call Check sort function and print return status
        CheckSort(listL)
      
        # print(timingList)

    #   Return the time list
    return (timingList)

# Write a function for Python Array. It will have the following arguments (1) the set of problem sizes N, (2) your random number seed, (3) your random number minimum value (rand_min), and (4) your random number maximum value (rand_max). 
def PythonArrayList(problem_size, random_seed, rand_min, rand_max):
    """
    TimePythonArray function that creates a python array and times the sorting array
    Inputs: takes arguments of problem_size, random_seed, rand_min, rand_max
    Outputs: returns the list of times in timingList array
    Usage: a function that creates python arrays
    """
    timingList = []
    
    for n in problem_size:
        print("doArrayProblems, doing problem size = ", n)
        
        random.seed(random_seed)
        
        listL = array.array('i', [random.randint(rand_min, rand_max) for _ in range(n)])
        
        CheckSort(listL)
        t1 = time.monotonic()
        
        iSort(listL)
        t2 = time.monotonic()
 
        CheckSort(listL)
        timingList.append(t2 - t1)
        
        # print(timingList)
        
    return timingList

# Write a function for Numpy Array. It will have the following arguments (1) the set of problem sizes N, (2) your random number seed, (3) your random number minimum value (rand_min), and (4) your random number maximum value (rand_max). 
def NumpyArrayList(problem_size, random_seed, rand_min, rand_max):
    """
    TimeNumpyArray function that creates a numpy array and times the sorting array
    Inputs: ttakes arguments of problem_size, random_seed, rand_min, rand_max
    Outputs: returns the list of times in timingList array
    Usage: a function that creates numpy arrays
    """
    timingList = []
    for n in problem_size:
        print("doNumPyProblems, doing problem size = ", n)
        
        np.random.seed(random_seed)
        
        listL = np.random.randint(rand_min, rand_max, n)
        
        CheckSort(listL)
        t1 = time.monotonic()
        
        iSort(listL)
        t2 = time.monotonic()
 
        CheckSort(listL)
        timingList.append(t2 - t1)
        
    return timingList


# Write a function to plot your 3-variable bar chart.
def CreatePlot(problem_size, list_timings, array_timings, numpy_timings, widths, xcoords, names):
    """
    PlotData function that plots takes data and displays a graph
    Inputs: xcoords, labels, listTimings, arrayTimings, widths, names
    Outputs: Displays bar chart
    Returns: None
    Usage: Plots data and displays a graph
    """
    plt.figure()
    plt.bar(xcoords - widths, list_timings, widths, label='List', color="darkblue")
    plt.bar(xcoords, array_timings, widths, label='Array', color="lightblue")
    plt.bar(xcoords + widths, numpy_timings, widths, label='NumPy', color="goldenrod")
    
    plt.xlabel('Problem Size (N)')
    plt.ylabel('Elapsed Time (s)')
    plt.title('Insertion Sort Runtimes by Data Structure and Problem Size')
    plt.xticks(xcoords, problem_size)
    plt.legend(names, loc=2)
    
    plt.savefig("<Riel_Orque>Project_05.png", dpi = 600)
    plt.show()

# Write your main function.  Which will contain the follow:
def main():
    """
    Main function is the starting point of execution
    Inputs: variables N, Seed, RandomMin, RandomMax, width, xcoord, and variableNames
    Outputs: Displays a graph displaying the timing for each arrays
    Usage: initialize variables and call functions
    """
    # displays name and current time
    print("\nRiel Orque", time.asctime())
    
    # Setup constant variables; N, RandomMin, RandomMax, and Seed value
    N = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    seed = 22
    rand_min = 0
    rand_max = 9999
    width = 0.25
    xcoord = np.arange(len(N))
    variableNames = ['Python List', 'Python Arrays', 'NumPy Arrays']
    
    
    # Call your Function for Python Lists Timing
    pythonList = PythonList(N, seed, rand_min, rand_max)
    print("\n")

    # Call your Function for Python Array Timing
    arrayList = PythonArrayList(N, seed, rand_min, rand_max)
    print("\n")

    # Call your Function for Numpy Array Timing
    numpyList = NumpyArrayList(N, seed, rand_min, rand_max)
    print("\n")

    # Call CreatePlot() function with timing list and data size list.
    CreatePlot(N, pythonList, arrayList, numpyList, width, xcoord, variableNames)
    
# calls main() function
if __name__ == "__main__":
    main()
