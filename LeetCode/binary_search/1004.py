class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def is_possible(length):
            if length == 0:
                return True

            n_zeros = 0
            for i in range(length):
                if nums[i] == 0:
                    n_zeros += 1

            if n_zeros <= k:
                return True

            for i in range(length, len(nums)):
                if nums[i] == 0:
                    n_zeros += 1

                if nums[i-length] == 0:
                    n_zeros -= 1

                if n_zeros <= k:
                    return True

            return False

        left = 0
        right = len(nums)
        answer = 0

        while left <= right:
            mid = (left+right) // 2

            if is_possible(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
