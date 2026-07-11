# https://leetcode.com/problems/decompress-run-length-encoded-list/description/

class Solution(object):
    # better solution
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # [freq, value]
        ans = []        
        for i in range(1, len(nums), 2):
            freq = nums[i-1]
            val = nums[i]
            temp = [val]*freq
            ans += temp
        return ans

    # original
    def decompressRLElist2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # [freq, value]
        ans = []        
        for i in range(1, len(nums), 2):
            freq = nums[i-1]
            val = nums[i]
            while freq > 0:
                ans.append(val)
                freq -= 1
        return ans

        