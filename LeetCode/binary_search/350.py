class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        answer = []
        used = {}

        for num in nums1:
            l_idx = bisect_left(nums2, num)
            r_idx = bisect_right(nums2, num)

            if l_idx == r_idx:
                continue

            used_cnt = used.get(num, 0)
            if l_idx + used_cnt < r_idx:
                answer.append(num)

                used[num] = used_cnt + 1

        return answer
