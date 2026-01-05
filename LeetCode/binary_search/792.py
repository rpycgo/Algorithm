class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_positions = defaultdict(list)
        for i, char in enumerate(s):
            char_positions[char].append(i)

        answer = 0
        for word in words:
            prev_idx = -1

            found = True
            for char in word:
                positions = char_positions.get(char, [])

                idx = bisect_right(positions, prev_idx)
                if idx == len(positions):
                    found = False
                    break

                prev_idx = positions[idx]

            if found:
                answer +=1

        return answer
