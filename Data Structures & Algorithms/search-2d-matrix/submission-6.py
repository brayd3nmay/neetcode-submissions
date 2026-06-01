class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                l, r = 0, len(matrix[mid]) - 1
                while l <= r:
                    m = l + ((r - l) // 2)
                    if target < matrix[mid][m]:
                        r = m - 1
                    elif target > matrix[mid][m]:
                        l = m + 1
                    else:
                        return True
                return False
        return False