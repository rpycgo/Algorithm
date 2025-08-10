class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num not in counts:
                counts.update({num: 1})
            else:
                counts[num] += 1

        max_value = max(counts.values())

        for key, value in counts.items():
            if value == max_value:
                return key
