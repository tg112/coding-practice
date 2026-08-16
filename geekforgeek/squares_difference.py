"""
https://www.geeksforgeeks.org/problems/squares-difference0939/1

Given an integer n, find the absolute difference between sum of the squares of first n natural numbers and square of sum of first n natural numbers.

Examples: 

Input: n = 2
Output: 4 
Explanation: abs|(12 + 22) - (1 + 2)2| = 4.

Input: n = 3
Output: 22
Explanation: abs |(12 + 22 + 32) - (1 + 2 + 3)2| = 22.
"""
class Solution:
    def squaresDiff(self, n):
        # code here
        sum_of_squares = 0
        suqure_of_sum = 0
        
        for i in range(1, n + 1):
            sum_of_squares += i ** 2
            suqure_of_sum += i
        return abs(sum_of_squares - (suqure_of_sum ** 2))
            