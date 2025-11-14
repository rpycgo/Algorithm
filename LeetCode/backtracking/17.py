class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs','8': 'tuv', '9': 'wxyz'
            }

        answer = []
        self.backtrack(answer, 0, "", digits, digit_to_letters)

        return answer

    def backtrack(self, answer, index, path, digits, digit_to_letters):
        if index == len(digits):
            answer.append(path)

            return

        for letter in digit_to_letters[digits[index]]:
            self.backtrack(answer, index + 1, path + letter, digits, digit_to_letters)

        return answer
