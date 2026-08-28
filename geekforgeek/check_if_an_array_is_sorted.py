"""
https://www.geeksforgeeks.org/dsa/program-check-array-sorted-not-iterative-recursive/

Given an array arr[], check if it is sorted in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

Examples: 

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.

Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted.
"""
class Solution:
    def isSorted(self, arr):
        left = 0
        while left < len(arr) - 1:
            if arr[left] > arr[left+1]:
                return False
            left += 1
        return True
