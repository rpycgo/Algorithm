class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}

        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            running_sum %= k

            if running_sum in remainder_map:
                if i - remainder_map[running_sum] >= 2:
                    return True
            else:
                remainder_map[running_sum] = i

        return False
