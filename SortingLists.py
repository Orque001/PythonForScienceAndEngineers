#!/usr/bin/env python3/Users/riel/Desktop/Python/PythonForScienceAndEngineers/SortingLists.py
# -*- coding: utf-8 -*-
"""
Inputs: user input integer N,(problem size), integer S(random number seed)
Outputs: prints out an unsorted list of random numbers and a sorted list of random numbers
Dependencies: import time module, import random module
Assumptions: Developed and tested using Spyder, Python version 3.11 on MacOS M1

@author: rielorque
"""
import time
import random

def unsortedList(aList):
    """ This function displays the unsorted list of random numbers
        Inputs: a list of numbers, aList
        Output: Prints an unsorted list of random numbers
        Returns: 
        Usage:
    """
    print("\nUnsorted List:")
    for i in range(len(aList)):
        print(aList[i], end=" ")
        
        if((i + 1) % 8 == 0):
            print() 
            
def sortedList(aList):
    """ This function displays a sorted list from least to greatest.
        Inputs: a list of numbers, sort function
        Output: sort function that sorts the list and print the sorted list
        Returns:
        Usage: sort function
    """
    aList.sort(reverse = False)
    print("\n")
    print("\nSorted List:")
    for i in range(len(aList)):
        print(aList[i], end=" ")
        
        if((i + 1) % 10 == 0):
            print()
def main():
    """
    Main function is the starting point of execution
    Inputs: variables integerN, integerS, and listL
    Outputs: Displays an unsorted and sorted random numbers list
    Usage: prompt user for an input of problem size and random number seed then display an unsorted and sorted list
    """
    # displays name and current time
    print("\nRiel", time.asctime())

    # prompt user to input an integer N for problem size and S for random number seed
    integerN = int(input("\nPlease enter an integer N (problem size): "))
    integerS = int(input("\nPlease enter an integer S (random number seed): "))
    
    # random seed
    random.seed(integerS)

    # listL variable to get a random int of 1-99 in the range of integerS
    listL = [random.randint(1, 99) for i in range(integerN)]

    # call functions
    unsortedList(listL)
    sortedList(listL)
    
    
# calls main() function
if __name__ == "__main__":
    main()

