class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))

        difficulty = [job[0] for job in jobs]

        profit = [job[1] for job in jobs]
        for i in range(1, len(profit)):
            profit[i] = max(profit[i], profit[i-1])

        answer = 0
        for worker_ in worker:
            idx = bisect_right(difficulty, worker_)

            if idx != 0:
                answer += profit[idx-1]

        return answer
