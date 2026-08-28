"""
Given a list of names in an array arr[] of size N, display the longest name contained in it.
If there are multiple longest names print all of that.

Examples:

Input: arr[] = {"GeeksforGeeks", "FreeCodeCamp", "StackOverFlow",  "MyCodeSchool"}
Output: GeeksforGeeks StackOverFlow
Explanation: size of arr[0] and arr[2] i.e., 13 > size of arr[1]  and arr[3] i.e., 12


Input:  arr[] = {"Akash", "Adr"}
Output: Akash
"""

def display_longest_name(arr):
    max_length = len(max(arr))
    for word in arr:
        if len(word) == max_length:
            print(word, end=" ")
