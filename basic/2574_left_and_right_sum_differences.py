# https://leetcode.com/problems/left-and-right-sum-differences/description/

class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n

        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        ans = []

        for i in range(n):
            ans.append(abs(left_sum[i] - right_sum[i]))

        return ans

    def solution_2(self, nums):
        left_sum = 0
        right_sum = sum(nums)
        ans = []

        for num in nums:
            right_sum -= num
            ans.append(abs(left_sum - right_sum))
            left_sum += num
        return ans
            