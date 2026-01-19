class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels =('a', 'i', 'e', 'o', 'u')

        n_vowels = 0
        n_consonants = 0

        for char in s:
            if char.isalpha():
                if char in vowels:
                    n_vowels += 1
                else:
                    n_consonants += 1

        answer = floor(n_vowels/n_consonants) if n_consonants != 0 else 0

        return answer
