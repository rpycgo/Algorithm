class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calculate_max_area(heights):
            stack = []
            curr_max_area = float('-inf')

            for i, curr_h in enumerate(heights):
                while stack and curr_h <= heights[stack[-1]]:
                    target_idx = stack.pop()
                    height = heights[target_idx]

                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1

                    curr_max_area = max(curr_max_area, height*width)

                stack.append(i)

            return curr_max_area

        n_r, n_c = len(matrix), len(matrix[0])
        heights = [0] * (n_c+1)
        max_area = float('-inf')

        for i in range(n_r):
            for j in range(n_c):
                if matrix[i][j] == '1':
                    heights[j] += int(matrix[i][j])
                else:
                    heights[j] = 0

            max_area = max(max_area, calculate_max_area(heights))

        return max_area
