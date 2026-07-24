class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        # 右上（1行目の最右列）からスタート
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True
            elif current > target:
                # 探している値より大きいので、この列には存在しない -> 左の列へ
                col -= 1
            else:
                # 探している値より小さいので、この行には存在しない -> 下の行へ
                row += 1

        return False