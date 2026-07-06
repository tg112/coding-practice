# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        ans = 0
        for num in sorted_nums:
            if num < k:
                ans +=1
        return ans
        