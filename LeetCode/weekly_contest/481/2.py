class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        hash_map = defaultdict(int)

        for char, cost_ in zip(s, cost):
            hash_map[char] += cost_

        if len(hash_map) == 1:
            return 0

        values = hash_map.values()

        answer = sum(values) - max(values)

        return answer
