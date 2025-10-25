class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        for char in text:
            count[char] += 1

        answer = min(count['b'], count['a'], count['l']//2, count['o']//2, count['n'])

        return answer
