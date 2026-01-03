class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        max_distance = 0
        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            max_distance = max(
                max_distance,
                abs(curr_max - min_val),
                abs(max_val - curr_min),
            )

            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)

        return max_distance
