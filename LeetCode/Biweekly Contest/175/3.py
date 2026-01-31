class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def get_lis_length(arr):
            if not arr:
                return 0

            LIS = []
            for x in arr:
                idx = bisect.bisect_left(LIS, x)

                if idx < len(LIS):
                    LIS[idx] = x
                else:
                    LIS.append(x)

            return len(LIS)

        max_len = 0
        for k in range(31):
            filtered = [num for num in nums if (num >> k) & 1]

            max_len = max(max_len, get_lis_length(filtered))

        return max_len
