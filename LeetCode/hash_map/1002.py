class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = defaultdict(int)
        for char in words[0]:
            common_count[char] += 1

        for word in words[1:]:
            current = defaultdict(int)
            for char in word:
                current[char] += 1

            for key in list(common_count.keys()):
                common_count[key] = min(common_count[key], current[key])

                if common_count[key] == 0:
                    del common_count[key]

        result = []
        for char, count in common_count.items():
            result.extend([char] * count)

        return result
