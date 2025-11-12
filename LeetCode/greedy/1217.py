class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(num%2 == 0 for num in position)
        odd = len(position) - even

        return min(even, odd)
