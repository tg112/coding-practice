# https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    ans += mat[i][j]

        for i in range(len(mat)):
            print(i,len(mat)-1-i)
            ans += mat[i][len(mat)-1-i] 
            
        if len(mat) % 2 == 1:
            ans = ans - mat[len(mat)/2][len(mat)/2]
        return ans
