class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        i = 0
        start = 0
        end = len(s)

        while i < len(s):
            if s[i] == 'I':
                answer.append(start)
                start += 1
                i += 1
            else:
                answer.append(end)
                end -= 1
                i += 1

        answer.append(start)

        return answer
