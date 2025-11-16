class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
            if i > start and candidates[i] == candidates[i-1]:
                continue

            path.append(candidates[i])

            self.backtrack(answer, candidates[i+1:], target - candidates[i], start, path)

            path.pop()
