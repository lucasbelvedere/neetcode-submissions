class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A): # ensures that A is always the smallest array
            A, B = B, A

        left, right = 0, len(A)
        while left <= right:
            i = (left + right) // 2
            j = half - i

            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i]     if i < len(A) else float("inf")

            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j]     if j < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min (Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1