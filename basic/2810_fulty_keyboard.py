# https://leetcode.com/problems/faulty-keyboard/

class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""

        for char in s:
            if char != "i":
                ans += char
            else:
                ans = ans[::-1]
        return ans
