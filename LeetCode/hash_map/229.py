class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] +=1

        answer = [
            key
            for key, value
            in hash_map.items()
            if value > int(len(nums)/3)
        ]

        return answer
