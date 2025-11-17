class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        
        self.backtrack(nums, 0, 0, target)

        return self.count
    
    def backtrack(self, nums, i, current_sum, target):
        if i == len(nums):
            if current_sum == target:
                self.count += 1
            return
        
        self.backtrack(nums, i+1, current_sum+nums[i], target)
        self.backtrack(nums, i+1, current_sum-nums[i], target)
