#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inputs: User inputs the size of the list, and size of the random number seed
Outputs: Outputs the unsorted and sorted list and displays if list is sorted or not
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
        Returns: Nothing
        Usage:
    """
    # prints unsorted list
    print("\nUnsorted List:")
    
    # for loop to loop through the list and print list
    for i in range(len(aList)):
        print(aList[i], end=" ")
        
        # prints 8 numbers per line
        if((i + 1) % 8 == 0):
            print() 


def checkSort(aList):
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
    return print("\nIs this list sorted? ", status) 

def sortedList(aList):
    """ This function displays a sorted list from least to greatest.
        Inputs: a list of numbers, sort function
        Output: sort function that sorts the list and print the sorted list
        Returns:
        Usage: sort function
    """
    # sort function to sort list
    aList.sort(reverse = False)
    
    # prints the sorted list
    print("\nSorted List:")
    for i in range(len(aList)):
        print(aList[i], end=" ")
        
        # prints 10 numbers per line
        if((i + 1) % 10 == 0):
            print()
    
def iSort(a):
    for i in range(1, len(a)):
        candidate = a[i]
        j = i - 1
        
        while(j >= 0 and a[j] > candidate):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = candidate

def main():
    """
    Main function is the starting point of execution
    Inputs: variables N, S, L1, xcoord
    Outputs: displays if the list is sorted or not
    Usage: main function
    """
    # displays name and current time
    print("\nRiel", time.asctime())

    # prompt user to input an integer N for problem size and S for random number seed
    N = int(input("\nSize of list wanted: "))
    S = int(input("\nRandom number seed: "))
    # randpm seed function
    random.seed(S)

    # list variable L1
    L1 = [random.randint(0, 99) for i in range(N)]
    
    # call functions
    unsortedList(L1)
    status = checkSort(L1)
    print(status)

    sortedList(L1)
    status = checkSort(L1)
    print(status)

    iSort(L1)
    status = iSort(L1)
    print(status)
   
    
# calls main() function
if __name__ == "__main__":
    main()




