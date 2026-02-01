class Solution:
    def countMonobit(self, n: int) -> int:
        cnt = 1
        curr_val = 1

        while curr_val <= n:
            cnt += 1
            curr_val = (curr_val << 1) | 1

        return cnt
