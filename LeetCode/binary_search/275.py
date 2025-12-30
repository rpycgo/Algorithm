class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        answer = 0

        while left <= right:
            mid = (left+right) // 2

            if n - mid <= citations[mid]:
                answer = n - mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
