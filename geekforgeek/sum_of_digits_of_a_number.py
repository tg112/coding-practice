"""
https://www.geeksforgeeks.org/dsa/program-for-sum-of-the-digits-of-a-given-number/
Given a number n, find the sum of its digits.

Examples : 

Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21

Input: n = 12
Output: 3
Explanation: The sum of its digits are: 1 + 2 = 3
"""
def sumOfDigits(n):
    # define variable for return value
    total = 0

    # iterate until n != 0
    while n != 0:
    # In order to make addtional value, generate remainder dividing by 10
        remainder = n % 10
    # Add Remainder to total
        total += remainder
    # For next interation, I want to divide the number by 10
        n = n // 10
    # return value
    return total
