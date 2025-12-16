class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        encode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

        seen = set()
        repeated = set()

        mask = 0
        for i, char in enumerate(s):
            mask = ((mask << 2) | encode[char]) & ((1 << 20) - 1)

            if i >= 9:
                if mask in seen:
                    repeated.add(s[i-9:i+1])
                else:
                    seen.add(mask)

        answer = list(repeated)

        return answer
