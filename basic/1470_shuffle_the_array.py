# https://leetcode.com/problems/shuffle-the-array/description/

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        first_half = nums[:n]
        ans = []
        for i in range(0, len(first_half)):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
