class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = defaultdict(int)
        for word in s1.split():
            count[word] += 1
        for word in s2.split():
            count[word] += 1

        answer = [key for key, value in count.items() if value == 1]

        return answer
