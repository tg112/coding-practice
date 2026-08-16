# https://www.geeksforgeeks.org/problems/mean0021/1
import math

class Solution:
    def findMean(self, arr):
        # code here 
        total = 0
        for num in arr:
            total += num
        return math.floor(total / len(arr))
    