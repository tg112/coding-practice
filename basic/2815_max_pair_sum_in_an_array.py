# https://leetcode.com/problems/max-pair-sum-in-an-array/description/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        best = {}

        for num in nums:
            digit = self.max_digit(num)

            if digit in best:
                ans = max(ans, best[digit] + num)
                best[digit] = max(best[digit], num)
            else:
                best[digit] = num

        return ans

    def max_digit(self, num: int) -> int:
        largest = 0

        while num:
            largest = max(largest, num % 10)
            num //= 10

        return largest
