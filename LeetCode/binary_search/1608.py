class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)
        answer = -1

        while left <= right:
            mid = (left+right) // 2

            idx = bisect_left(nums, mid)
            count = len(nums) - idx

            if count == mid:
                return mid
            elif count >= mid:
                left = mid + 1
            else:
                right = mid - 1

        return answer
