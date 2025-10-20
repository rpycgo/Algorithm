class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        original_nums = nums.copy()
        nums = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        top_k_index = []
        top_k = []

        while len(top_k_index) != k:
            _, i = heapq.heappop(nums)

            top_k_index.append(i)

        top_k_index.sort()
        top_k = [original_nums[i] for i in top_k_index]

        return top_k
