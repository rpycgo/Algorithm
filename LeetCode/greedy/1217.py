class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if len(position) == 1:
            return 0

        count = defaultdict(int)
        for num in position:
            if num%2 == 0:
                count['even'] += 1
            else:
                count['odd'] += 1

        if len(count) == 1:
            return 0

        answer = min(count.values())

        return answer
