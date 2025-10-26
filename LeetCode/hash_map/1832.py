class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = defaultdict(int)
        for char in sentence:
            count[char] += 1

        answer = len([value for value in count.values() if value > 0])
        answer = True if answer == 26 else False

        return answer
