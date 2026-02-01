class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(left, right):
            if right-left <= 1:
                return 0

            mid = (left+right) // 2
            cnt = merge_sort(left, mid) + merge_sort(mid, right)

            i, j = mid, mid
            for left_val in prefix_sums[left:mid]:
                while i < right and prefix_sums[i]-left_val < lower:
                    i += 1
                while j < right and prefix_sums[j]-left_val <= upper:
                    j += 1

                cnt += (j - i)

            prefix_sums[left:right] = sorted(prefix_sums[left:right])

            return cnt

        n = len(nums)

        prefix_sums = [0] * (n+1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + nums[i]

        answer = merge_sort(0, n+1)

        return answer
