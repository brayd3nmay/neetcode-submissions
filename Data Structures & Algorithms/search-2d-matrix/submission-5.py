class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l, r = 0, len(matrix[mid])

                while l <= r:
                    m = (l + r) // 2

                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1

                return False
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        return False 