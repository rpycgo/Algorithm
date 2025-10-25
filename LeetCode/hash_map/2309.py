class Solution:
    def greatestLetter(self, s: str) -> str:
        lower_count = defaultdict(int)
        upper_count = defaultdict(int)

        for char in s:
            if 'a' <= char <= 'z':
                lower_count[char] += 1
            else:
                upper_count[char] += 1

        answer = []
        for i in range(97, 123):
            if lower_count[chr(i)] >= 1 and upper_count[chr(i-32)] >= 1:
                answer.append(chr(i-32))

        answer = max(answer) if answer else ''

        return answer
