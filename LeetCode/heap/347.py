class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts.update({num: 1})
            else:
                counts[num] += 1
        
        counts = [(-value, key) for key, value in counts.items()]
        heapq.heapify(counts)
        counts = heapq.nsmallest(k, counts)

        answer = [count for _, count in counts]

        return answer
