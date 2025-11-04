class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        num_not_allowed = 0

        for word in words:
            for char in word:
                if char not in allowed:
                    num_not_allowed += 1
                    break

        answer = len(words) - num_not_allowed

        return answer
