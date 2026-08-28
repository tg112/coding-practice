"""
https://www.geeksforgeeks.org/dsa/check-large-number-divisible-6-not/
Given a number, the task is to check if a number is divisible by 6 or not. 
The input number may be large and it may not be possible to store even if we use long long int.

Examples: 

Input  : n = 2112
Output: Yes

Input : n = 1124
Output : No

Input  : n = 363588395960667043875487
Output : No
"""
def isDivisibleBy6(n):
    isDivisible = n // 6
    return "Yes" if isDivisible == 0 else "No"
