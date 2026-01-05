class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def has_common_subarray(length):
            seen = set()

            for i in range(len(nums1)-length+1):
                window = tuple(nums1[i:i+length])
                seen.add(window)

            for j in range(len(nums2)-length+1):
                window = tuple(nums2[j:j+length])
                if window in seen:
                    return True

            return False

        left = 1
        right = min(len(nums1), len(nums2))

        answer = 0
        while left <= right:
            mid = (left+right) // 2

            if has_common_subarray(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
