# https://leetcode.com/problems/number-of-employees-who-met-the-target/description/
 
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                ans += 1   
        return ans
        