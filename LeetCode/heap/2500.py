class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i] = [-element for element in grid[i]]
            heapq.heapify(grid[i]) 

        maxes = 0
        while True:
            current_max = []
            for row in grid:
                pop_value = -heapq.heappop(row)
                current_max.append(pop_value)

            maxes = maxes + max(current_max)

            if not grid[0]:
                break

        return maxes
