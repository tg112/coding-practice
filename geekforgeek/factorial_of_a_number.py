"""
https://www.geeksforgeeks.org/problems/factorial5739/1

Given a non-negative integers n, compute the factorial of the given number. 
Factorial of n is defined as n * (n -1) * (n - 2) * ... * 1. For n = 0, the factorial is defined as 1.

Examples:

Input: n = 5
Output: 120
Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

Input: n = 4
Output: 24
Explanation: 4! = 4 * 3 * 2 * 1 = 24

Input: n = 0
Output: 1

Input: n = 1
Output: 1
"""
class Solution:
    def factorial(self, n: int) -> int:
        # code here
        # if n == 1:
        #     return 1
        # return n * self.factorial(n-1)
        total = 1
        for i in range(1, n + 1):
            total *= i
        return total
