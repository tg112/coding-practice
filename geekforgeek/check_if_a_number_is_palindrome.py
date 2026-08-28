
"""
https://www.geeksforgeeks.org/dsa/check-if-a-number-is-palindrome/
Given an integer n, determine whether it is a palindrome number or not. 
A number is called a palindrome if it reads the same from forward and backward.

Examples:

Input: n = 12321
Output: True
Explanation: 12321 is a palindrome number because it reads same  forward and backward.

Input: n = -121
Output: True
Explanation:  We number is palindrome, we mainly ignore sign.

Input: n = 1234
Output:  False
Explanation: 1234 is not a palindrome number because it does not read the same forward and backward.
"""
def isPalinfrome(num):
    left = 0
    right = len(str(num)) - 1

    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right -= 1
    return True 
