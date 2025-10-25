class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in set(nums1):
            count[num] += 1

        for num in set(nums2):
            count[num] += 1

        for num in set(nums3):
            count[num] += 1

        answer = [key for key, value in count.items() if value >= 2]

        return answer
