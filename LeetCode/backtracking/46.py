class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        used = [False] * len(nums)

        self.backtrack(answer, nums, [], used)

        return answer

    def backtrack(self, answer, nums, path, used):
        if len(path) == len(nums):
            answer.append(path[:])
            return

        for i, num in enumerate(nums):
            if not used[i]:
                path.append(num)
                used[i] = True

                self.backtrack(answer, nums, path, used)

                path.pop()
                used[i] = False
