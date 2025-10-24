from collections import defaultdict

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return char

        answer = [key for key, value in count.items() if value < 0]

        return answer[0]
