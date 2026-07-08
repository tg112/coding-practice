# https://leetcode.com/problems/count-items-matching-a-rule/description/

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        counter = 0
        for item in items:
            item_type = item[0]
            item_color = item[1]
            item_name = item[2]

            if ruleKey == "type" and item_type == ruleValue:
                counter += 1
            elif ruleKey == "color" and item_color == ruleValue:
                counter += 1
            elif ruleKey == "name" and item_name == ruleValue:
                counter += 1
        return counter
