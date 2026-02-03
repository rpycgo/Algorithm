class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i * i)
            i += 1

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            curr_sum, curr_cnt = queue.popleft()

            next_cnt = curr_cnt + 1

            for square in squares:
                next_sum = curr_sum + square

                if next_sum == n:
                    return next_cnt

                if next_sum < n and next_sum not in visited:
                    visited.add(next_sum)
                    queue.append((next_sum, next_cnt))

        return n
