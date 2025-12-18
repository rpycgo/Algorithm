class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = defaultdict(int)

        s = s.split()

        if len(pattern) != len(s):
            return False

        for char, word in zip(pattern, s):
            print(char, hash_map)
            if char not in hash_map:
                hash_map[char] = word
            elif hash_map[char] != word:
                return False

        if len(set(hash_map.keys())) != len(set(hash_map.values())):
            return False

        return True
