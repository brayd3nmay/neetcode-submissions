class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if (len(b) < len(a)):
            a, b = b, a

        total = len(a) + len(b)
        half = total // 2
        l, r = 0, len(a) - 1
        while True:
            a_mid = (l + r) // 2
            b_mid = half - a_mid - 2

            a_left = a[a_mid] if a_mid >= 0 else float("-infinity")
            a_right = a[a_mid + 1] if (a_mid + 1) < len(a) else float("infinity")
            b_left = b[b_mid] if b_mid >= 0 else float("-infinity")
            b_right = b[b_mid + 1] if (b_mid + 1) < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2 
            elif a_left > b_right:
                r = a_mid - 1
            else:
                l = a_mid + 1