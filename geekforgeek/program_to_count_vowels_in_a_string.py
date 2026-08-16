"""
https://www.geeksforgeeks.org/dsa/program-count-vowels-string-iterative-recursive/
Given a string, count the total number of vowels (a, e, i, o, u) in it. 
There are two methods to count total number of vowels in a string. 

Iterative 
Recursive
Examples: 

Input : abc de
Output : 2

Input : geeksforgeeks portal
Output : 7
"""
def count_vowels(words):
    vowels = ["a", "i", "u", "e", "o"]
    counter = 0

    for char in words:
        if char in vowels:
            counter += 1
    return counter

def r_count_vowels(words, counter = 0):
    if len(words) == 0:
        return counter
    vowels = ["a", "i", "u", "e", "o"]
    if words[0] in vowels:
        counter += 1
    return r_count_vowels(words[1:], counter)
    
    
