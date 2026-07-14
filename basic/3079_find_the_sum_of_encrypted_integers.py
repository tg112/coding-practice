# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            max_digit = 0
            digit_count = 0
            while num > 0:
                digit = num % 10
                max_digit = max(max_digit, digit)
                digit_count += 1
                num = num // 10
            encrypted = 0
            for i in range(digit_count):
                encrypted = encrypted * 10 + max_digit
            arr.append(encrypted)
        return sum(arr)
