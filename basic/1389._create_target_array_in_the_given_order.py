# https://leetcode.com/problems/create-target-array-in-the-given-order/description/

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(nums)):
            ans.insert(index[i], nums[i])
        return ans
