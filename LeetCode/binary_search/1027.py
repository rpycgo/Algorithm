class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)

        answer = 2
        min_val = min(nums)
        max_val = max(nums)

        for diff in range(min_val-max_val, max_val-min_val+1):
            visited = [False] * n

            for i in range(n):
                if visited[i]:
                    continue

                curr_idx = i
                curr_val = nums[i]
                length = 1

                while True:
                    next_val = curr_val + diff

                    if next_val not in pos:
                        break

                    idx_list = pos[next_val]
                    idx = bisect_right(idx_list, curr_idx)

                    if idx == len(idx_list):
                        break

                    curr_idx = idx_list[idx]
                    curr_val = next_val
                    visited[curr_idx] = True
                    length += 1

                answer = max(answer, length)

        return answer
