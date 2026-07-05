# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pairs = []
        print(pairs)

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] < target:
                    if i == j:
                        continue
                    pair = sorted([i,j])
                    if pair not in pairs:
                        pairs.append(pair)   
                    
        return len(pairs)