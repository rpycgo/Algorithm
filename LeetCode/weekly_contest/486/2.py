class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        negatives = [(i, num) for i, num in enumerate(nums) if num < 0]
        non_negatives = [num for num in nums if num >= 0]

        if len(negatives) == len(nums):
            return nums

        queue = deque(non_negatives)

        i = 0
        while i < k:
            item = queue.popleft()
            queue.append(item)

            i += 1

        answer = [float('inf')] * len(nums)
        for idx, val in negatives:
            answer[idx] = val

        idx = 0
        while queue:
            val = queue.popleft()

            while answer[idx] != float('inf'):
                idx += 1
            answer[idx] = val

        return answer
