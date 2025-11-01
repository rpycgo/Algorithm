class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(heap)

        answer = ''
        while heap:
            value, key = heapq.heappop(heap)
            answer += (-value*key)

        return answer
