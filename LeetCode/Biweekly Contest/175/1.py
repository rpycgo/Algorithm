class Solution:
    def reverseByType(self, s: str) -> str:
        answer = [-1] * len(s)

        special_characters = []
        special_character_idx = []
        lowercase_letters = []
        for i, char in enumerate(s):
            if char.isalpha():
                lowercase_letters.append(char)
            else:
                special_characters.append(char)
                special_character_idx.append(i)

        for char, i in zip(special_characters, reversed(special_character_idx)):
            answer[i] = char

        idx = 0
        for char in reversed(lowercase_letters):
            while answer[idx] != -1:
                idx += 1

            answer[idx] = char

        answer = ''.join(answer)

        return answer
