# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_len = 0

        for sentence in sentences:
            max_len = max(max_len, len(sentence.split()))
        return max_len
