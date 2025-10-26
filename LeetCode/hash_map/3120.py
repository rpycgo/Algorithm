class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = defaultdict(int)
        for char in word:
            count[char] += 1

        answer = [
            chr(i)
            for i
            in range(97, 123)
            if count[chr(i)] and count[chr(i-32)]
        ]
        answer = len(answer)

        return answer
