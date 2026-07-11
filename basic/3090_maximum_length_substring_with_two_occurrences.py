# 3090. Maximum Length Substring With Two Occurrences

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                count = {}
                is_valid_substring = True

                for k in range(i, j):
                    c = s[k]
                    count[c] = count.get(c, 0) + 1

                    if count[c] > 2:
                        is_valid_substring = False
                        break

                if is_valid_substring:
                    ans = max(ans, j - i)

        return ans
