"""
Program to print the given digit in words
Given a number N, the task is to convert every digit of the number into words.

Examples: 

Input: N = 1234 
Output: One Two Three Four 
Explanation: 
Every digit of the given number has been converted into its corresponding word.

Input: N = 567 
Output: Five Six Seven 
"""

def toStringNumber(num):
    num_map = {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    return num_map[num]

def printValue(num):
    str_num = str(num)
    for num in str_num:
        print(toStringNumber(num), end=" ")


printValue(1234)
