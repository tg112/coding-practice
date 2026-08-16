class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        sorted_nums = sorted(nums)
        
        for i in range(len(nums)):
            if sorted_nums[i] == target:
                ans.append(i)
        return ans
