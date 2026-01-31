class Solution:
    def minimumK(self, nums: List[int]) -> int:
        def nonPositive(nums, k):
            cnt = 0
            for num in nums:
                cnt += ((num-1)//k + 1)

            return True if cnt <= k**2 else False

        left = 1
        right = 10 ** 10

        answer = right
        while left <= right:
            mid = (left+right) // 2

            if nonPositive(nums, mid):
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer
