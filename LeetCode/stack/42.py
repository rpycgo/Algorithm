class Solution:
    def trap(self, height: List[int]) -> int:
        height = height + [0]

        stack = []
        total_trap = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                target_idx = stack.pop()

                if not stack:
                    break

                curr_w = i - stack[-1] - 1
                curr_h = min(height[i], height[stack[-1]]) - height[target_idx]
                total_trap += (curr_w*curr_h)

            stack.append(i)

        return total_trap
