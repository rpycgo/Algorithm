class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def can_find_subarray(length):
            for start in range(n-length+1):
                if prefix[start+length] - prefix[start] >= target:
                    return True
            return False

        n = len(nums)

        prefix = [0] * (n+1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num

        left = 1
        right = n
        answer = 0

        while left <= right:
            mid = (left+right) // 2

            if can_find_subarray(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
