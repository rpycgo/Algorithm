class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, number in enumerate(numbers):
            complement = target - number

            complement_idx = bisect_left(numbers, complement, i+1)

            if complement_idx < len(numbers) and numbers[complement_idx] == complement:
                return [i+1, complement_idx+1]
