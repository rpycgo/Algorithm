class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        stack = [0]
        max_area = 0

        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                max_area = max(max_area, h*w)

            stack.append(i)

        return max_area
