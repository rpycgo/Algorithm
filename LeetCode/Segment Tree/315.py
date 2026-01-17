class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(list(set(nums)))
        rank_map = {val: i for i, val in enumerate(sorted_nums)}

        m = len(sorted_nums)
        h = m.bit_length()
        size = 1 << h

        tree = [0] * (size * 2)

        def query(left, right):
            left += size
            right += size

            total = 0
            while left <= right:
                if left%2 == 1:
                    total += tree[left]
                    left += 1

                if right%2 == 0:
                    total += tree[right]
                    right -= 1

                left //= 2
                right //= 2

            return total 

        def update(idx, val):
            idx += size
            tree[idx] += val

            while idx > 2:
                idx //= 2
                tree[idx] = tree[idx*2] +  tree[idx*2 + 1]

        answer = []
        for x in reversed(nums):
            rank = rank_map[x]
            result = query(0, rank-1)
            answer.append(result)

            update(rank, 1)

        answer = answer[::-1]

        return answer
