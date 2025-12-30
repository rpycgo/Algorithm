class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        answer = []
        for query in queries:
            idx = bisect_right(prefix, query) - 1

            answer.append(idx)

        return answer
