# https://leetcode.com/problems/shortest-distance-to-a-character/description/
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n

        prev = float('-inf')

        # left to right
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        prev = float('inf')

        # right to left
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans