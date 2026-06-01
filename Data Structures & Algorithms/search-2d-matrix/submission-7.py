class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            row = mid // COLS
            col = mid % COLS
            if target > matrix[row][col]:
                left = mid + 1
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                return True
        return False