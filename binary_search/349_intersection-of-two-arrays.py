class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        set_num1 = set(nums1)
        set_num2 = set(nums2)

        larger_set = None
        smaller_set = None
        if len(set_num1) < len(set_num2):
            larger_set = set_num2
            smaller_set = set_num1
        else:
            larger_set = set_num1
            smaller_set = set_num2


        for val in larger_set:
            if val in smaller_set:
                ans.append(val)
        return ans
