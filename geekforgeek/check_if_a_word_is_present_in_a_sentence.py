"""
Given a sentence as a string str and a word word, the task is to check if the word is present in str or not. 
A sentence is a string comprised of multiple words and each word is separated with spaces.

Examples: 
Input: str = "Geeks for Geeks", word = "Geeks" 
Output: Word is present in the sentence 

Input: str = "Geeks for Geeks", word = "eeks" 
Output: Word is not present in the sentence 
"""

def isWordPresent(sentence, word):
    arr = sentence.split(" ")
    if word in arr:
        print("Word is present in the sentence")
    else:
        print("Word is not present in the sentence")

isWordPresent("Geeks for Geeks", "eeks")
