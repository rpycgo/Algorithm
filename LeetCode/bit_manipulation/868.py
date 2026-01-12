class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_pos = -1
        curr_pos = 0

        while n > 0:
            if n & 1:
                if last_pos != -1:
                    max_gap = max(max_gap, curr_pos-last_pos)
                
                last_pos = curr_pos

            n >>= 1
            curr_pos += 1

        return max_gap
