class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        results = nums.copy()
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)

        count = 0
        while count != k:
            minimum_value, i = heapq.heappop(nums)
            new_value = minimum_value * multiplier
            results[i] = new_value

            heapq.heappush(nums, (new_value, i))

            count +=1

        return results
