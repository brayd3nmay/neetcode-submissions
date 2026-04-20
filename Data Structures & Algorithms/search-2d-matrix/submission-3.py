class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] <= target <= matrix[mid][COLS - 1]:
                l, r = 0, COLS - 1
                while l <= r:
                    m = (l + r) // 2

                    if target == matrix[mid][m]:
                        return True
                    elif target < matrix[mid][m]:
                        r = m - 1
                    else:
                        l = m + 1
                return False
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                top = mid + 1
        return False