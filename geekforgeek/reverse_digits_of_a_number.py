"""
https://www.geeksforgeeks.org/dsa/write-a-program-to-reverse-digits-of-a-number/

Given an Integer n, find the reverse of its digits.

Examples:  

Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221.

Input: n = 200
Output: 2
Explanation: By reversing the digits of number, number will change into 2.

Input: n = 12345 
Output: 54321
Explanation: By reversing the digits of number, number will change into 54321.
"""

class Solution:
	def reverseDigits(self, n):
		# Code here
		reversed_n = ""
		while n != 0:
			remainder = n % 10
			reversed_n = reversed_n + str(remainder)
			n = n // 10
		return int(reversed_n)
		    