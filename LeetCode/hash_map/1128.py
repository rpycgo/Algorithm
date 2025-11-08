class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        for domino in dominoes:
            domino.sort()

            count[tuple(domino)] += 1

        answer = sum([
            value*(value-1) // 2
            for value
            in count.values()
            if value >= 2
        ])

        return answer
