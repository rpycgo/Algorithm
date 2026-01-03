class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            count = Counter(nums)

            answer = 0
            for num in count:
                if count[num] > 1:
                    answer += 1

            return answer

        nums.sort()

        answer = 0
        prev_num = None

        for num in nums:
            if prev_num == num:
                continue

            idx = bisect_left(nums, num+k)

            if idx < len(nums) and nums[idx] == num+k:
                answer += 1

            prev_num = num

        return answer
