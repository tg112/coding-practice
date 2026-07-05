# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(words) != len(s):
            return False
        
        for i, char in enumerate(s):
            if words[i][0] != char:
                return False
        return True
        