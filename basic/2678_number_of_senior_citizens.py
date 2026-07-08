# https://leetcode.com/problems/number-of-senior-citizens/description/

class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        ans = 0
        for detail in details:
            age = detail[11:13]
            if int(age) > 60:
                ans += 1
        return ans
