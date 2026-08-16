# https://www.geeksforgeeks.org/dsa/count-number-even-odd-elements-array/
class Solution:
	def countOddEven(self, arr):
		even_number = 0
		odd_number = 0
		for num in arr:
			if num % 2 == 0:
				even_number += 1
			else:
				odd_number += 1
		return odd_number, even_number
