class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnas = defaultdict(int)

        for i in range(len(s)-10+1):
            dnas[s[i:i+10]] += 1

        answer = [key for key, value in dnas.items() if value >= 2]

        return answer
