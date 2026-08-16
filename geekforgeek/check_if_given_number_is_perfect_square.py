"""
https://www.geeksforgeeks.org/dsa/check-if-given-number-is-perfect-square-in-cpp/

Given a number n, determine whether it is a perfect square. 
Return true if it is a perfect square; otherwise, return false.

Examples : 

Input :  n = 36
Output :  true
Explanation:  Since 6 × 6 = 36, therefore 36 is a perfect square.

Input:  n = 2500
Output:  true
Explanation:  Since 50 × 50 = 2500, therefore 2500 is a perfect square.

Input:  n = 8
Output:  false
Explanation:  No integer multiplied by itself equals 8, so 8 is not a perfect square.
"""
import math

class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        # code here
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return (root * root) == n

