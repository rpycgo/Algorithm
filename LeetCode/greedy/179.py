class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        n = len(nums_str)

        for i in range(n):
            for j in range(0, n - i -1):
                if nums_str[j] + nums_str[j+1] < nums_str[j+1] + nums_str[j]:
                    nums_str[j], nums_str[j+1] = nums_str[j+1], nums_str[j]

        answer = ''.join(nums_str)
        answer = '0' if answer[0] == '0' else answer

        return answer
