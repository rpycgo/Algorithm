class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        visited = {0}

        queue = deque([(0, 0)])
        while queue:
            curr_coin, curr_cnt = queue.popleft()

            next_cnt = curr_cnt + 1

            for coin in coins:
                next_coin = curr_coin + coin

                if next_coin == amount:
                    return next_cnt

                if next_coin < amount and next_coin not in visited:
                    visited.add(next_coin)
                    queue.append((next_coin, next_cnt))

        return -1
