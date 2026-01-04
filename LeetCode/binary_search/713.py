class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        log_k = log(k)
        eps = 1e-10

        prefix = [0.0]
        for num in nums:
            prefix.append(prefix[-1] + log(num))

        answer = 0
        for right in range(n):
            target = prefix[right+1] - log_k
            idx = bisect_right(prefix, target + eps)
            answer += (right+1) - idx

        return answer
