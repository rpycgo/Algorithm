class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1

        count = count.values()
        answer = True if len(count) == len(set(count)) else False

        return answer
