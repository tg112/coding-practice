# https://leetcode.com/problems/furthest-point-from-origin/description/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        symbols = {
            "L": -1,
            "R": 1,
            "_": 0 
        }
        distance = 0
        num_of_underscore = 0

        for move in moves:
            distance += symbols[move]
            if move == "_":
                num_of_underscore += 1
        return abs(distance) + num_of_underscore