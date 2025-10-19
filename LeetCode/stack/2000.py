class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        is_match = False
        for i, char in enumerate(word):
            stack.append(char)

            if char == ch:
                is_match = True
                break

        stack = stack[::-1] if is_match else stack

        result = ''.join(stack) + word[i+1:]

        return result
