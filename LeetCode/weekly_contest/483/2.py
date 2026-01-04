class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        starts_with = defaultdict(list)
        for word in words:
            starts_with[word[0]].append(word)

        results = []
        n = len(words)

        for i in range(n):
            top = words[i]

            for left in starts_with[top[0]]:
                if left == top:
                    continue

                for right in starts_with[top[3]]:
                    if right == top or right == left:
                        continue

                    for bottom in starts_with[left[3]]:
                        if bottom in (top, left, right):
                            continue

                        if bottom[3] == right[3]:
                            results.append([top, left, right, bottom])

        results.sort()

        return results
