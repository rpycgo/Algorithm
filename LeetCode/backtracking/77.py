class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = range(1, n + 1)
        answer = []

        self.backtrack(answer, candidates, 0, [], k)

        return answer

    def backtrack(self, answer, candidates, start, path, k):
        if len(path) == k:
            answer.append(path[:])
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])

            self.backtrack(answer, candidates, i+1, path, k)

            path.pop()
