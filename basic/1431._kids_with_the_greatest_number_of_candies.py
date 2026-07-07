# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        candies_of_kids = []
        max_value = max(candies)
        for candie in candies:
            current_candies = candie + extraCandies
            candies_of_kids.append(current_candies >= max_value)
        return candies_of_kids
        

        