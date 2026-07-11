# https://leetcode.com/problems/apple-redistribution-into-boxes/description/
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ans = 0
        total_apples = sum(apple)

        for num in sorted(capacity, reverse=True):
            ans += 1
            total_apples = total_apples - num
            if total_apples <= 0:
                break
        return ans
        