class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        answer = -1
        for key, value in count.items():
            if value == 1:
                answer = s.find(key)

                break

        return answer
