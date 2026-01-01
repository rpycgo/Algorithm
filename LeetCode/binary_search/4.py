class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            i = (left+right) // 2
            j = (m+n+1) // 2 - i

            left_a = nums1[i-1] if i > 0 else float('-inf')
            right_a = nums1[i] if i < m else float('inf')
            left_b = nums2[j-1] if j > 0 else float('-inf')
            right_b = nums2[j] if j < n else float('inf')

            if left_a <= right_b and left_b <= right_a:
                if (m+n) %2 == 1:
                    return max(left_a, left_b)
                else:
                    return (max(left_a, left_b) + min(right_a, right_b)) / 2
            elif left_a > right_b:
                right = i - 1
            else:
                left = i + 1
