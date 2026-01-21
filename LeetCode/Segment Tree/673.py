class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def merge(v1, v2):
            if v1[0] > v2[0]:
                return v1

            if v1[0] < v2[0]:
                return v2

            if v1[0] == v2[0]:
                return [v1[0], v1[1]+v2[1]]

        def update(idx, length, cnt):
            idx += size
            tree[idx] = merge(tree[idx], [length, cnt])

            while idx > 1:
                idx //= 2
                tree[idx] = merge(tree[idx*2], tree[idx*2 + 1])

        def query(left, right):
            left += size
            right += size

            result = [0, 0]
            while left <= right:
                if left%2 == 1:
                    result = merge(result, tree[left])
                    left += 1

                if right%2 == 0:
                    result = merge(result, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        sorted_nums = sorted(list(set(nums)))
        rank_map = {val: i for i, val in enumerate(sorted_nums)}

        m = len(sorted_nums)
        h = m.bit_length()

        size = 1 << h
        tree = [[0, 0] for _ in range(size*2)]

        for num in nums:
            rank = rank_map[num]

            prev_len, prev_cnt = query(0, rank-1)

            curr_len = prev_len + 1
            curr_cnt = max(prev_cnt, 1)

            update(rank, curr_len, curr_cnt)

        answer = tree[1][1]

        return answer
