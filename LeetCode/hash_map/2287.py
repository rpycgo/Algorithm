class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = defaultdict(int)

        for char in s:
            count[char] += 1

        answer = 0
        while True:
            for char in target:
                count[char] -= 1

            if any([count[char] < 0 for char in target]):
                break

            answer += 1

        return answer
