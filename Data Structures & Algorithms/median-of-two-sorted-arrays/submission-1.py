class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a) - 1
        while True:
            a_middle = (l + r) // 2
            b_middle = half - a_middle - 2
            
            a_left = a[a_middle] if a_middle >= 0 else float('-inf')
            a_right = a[a_middle + 1] if a_middle + 1 < len(a) else float('inf')
            b_left = b[b_middle] if b_middle >= 0 else float('-inf')
            b_right = b[b_middle + 1] if b_middle + 1 < len(b) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = a_middle - 1
            else:
                l = a_middle + 1