# https://leetcode.com/problems/truncate-sentence/

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = []

        for i, word in enumerate((s.split(" "))):
            if i >= k:
                break
            ans.append(word)
        return " ".join(ans)
    
    def truncateSentence2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split()
        return " ".join(words[:k])
