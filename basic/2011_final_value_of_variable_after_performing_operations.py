# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        operations_map = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1,
        }

        x = 0

        for operation in operations:
            x += operations_map[operation]
        return x
