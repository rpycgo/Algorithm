class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums1:
            count[num] += 1

        answer = []
        for num in nums2:
            if count[num] > 0:
                answer.append(num)

                count[num] -= 1

        return answer
