class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a)
        while True:
            i = (l + r) // 2
            j = half - i

            print(f"i: {i}")
            print(f"j: {j}")

            a_left = a[i - 1] if i - 1 >= 0 else float('-inf')
            a_right = a[i] if i < len(a) else float('inf')
            b_left = b[j - 1] if j - 1 >= 0 else float('-inf')
            b_right = b[j] if j < len(b) else float('inf')

            print(f"a_left: {a_left}")
            print(f"a_right: {a_right}")
            print(f"b_left: {b_left}")
            print(f"b_right: {b_right}")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (min(a_right, b_right) + max(a_left, b_left)) / 2
            elif a_left > b_right:
                r = i - 1
            else:
                l = i + 1
