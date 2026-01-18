class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        def manhattan_distance(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)

        towers.sort()

        max_quality = float('-inf')
        coord = [-1, -1]
        for tower in towers:
            x, y, quality = tower

            dist = manhattan_distance(x, y, center[0], center[1])
            if dist > radius:
                continue

            if quality > max_quality:
                max_quality = quality
                coord = [x, y]

        return coord
