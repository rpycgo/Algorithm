class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)
        for char in ransomNote:
            count[char] += 1

        for char in magazine:
            count[char] -= 1

        answer = all([True if value <= 0 else False for value in count.values()])

        return answer
