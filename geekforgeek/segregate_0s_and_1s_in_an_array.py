"""
Given an array arr[] consisting of only 0's and 1's. 
Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Input : arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input : arr[] = [0, 1, 0]  
Output :  [0, 0, 1] 

Input : arr[] = [1, 1]  
Output :  [1, 1] 

Input : arr[] = [0]  
Output :  [0] 
"""
from collections import Counter

class Solution:
    def segregate0and1(self, arr):
        map = Counter(arr)
        
        for i in range(map[0]):
            arr[i] = 0
        
        for i in range(map[0], len(arr)):
            arr[i] = 1
        return arr
