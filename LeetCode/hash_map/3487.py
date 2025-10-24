class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_array = set()
        for num in nums:
            if num not in unique_array:
                unique_array.add(num)
        
        unique_array = tuple(unique_array)
        all_negative = True
        for num in unique_array:
            if num > 0:
                all_negative = False

        if all_negative:
            answer = max(unique_array)
        else:
            answer = sum([num for num in unique_array if num > 0])

        return answer
