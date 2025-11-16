class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        values = count.values()

        answer = max(values) - min(values) if len(values) == 2 else max(values)

        return answer
