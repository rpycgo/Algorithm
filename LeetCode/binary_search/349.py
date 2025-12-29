class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        answer = set()

        for num in nums1:
            idx = bisect_left(nums2, num)

            if idx < len(nums2) and nums2[idx] == num:
                answer.add(num)

        answer = list(answer)

        return answer
