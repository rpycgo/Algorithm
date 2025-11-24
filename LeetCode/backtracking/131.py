class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        self.backtrack(answer, s, 0, [])

        return answer

    def backtrack(self, answer, s, start, path):
        if start == len(s):
            answer.append(path[:])
            return

        for i in range(start, len(s)):
            substring = s[start:i+1]

            if substring == substring[::-1]:
                path.append(substring)

                self.backtrack(answer, s, i+1, path)

                path.pop()
