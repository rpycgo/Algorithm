class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        count = count[k:]

        answer = sum([value for key, value in count])

        return answer
