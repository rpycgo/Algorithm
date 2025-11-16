class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        self.backtrack(answer, candidates, target, 0, [])

        return answer

    def backtrack(self, answer, candidates, target, start, path):
        if target == 0:
            answer.append(path[:])
            return

        if target < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])

            self.backtrack(answer, candidates, target - candidates[i], i, path)

            path.pop()
