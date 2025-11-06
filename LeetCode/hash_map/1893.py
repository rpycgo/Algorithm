class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        answer = [False] * right
        for range_ in ranges:
            start, end = range_
            
            for i in range(start-1, end):
                if i >= right:
                    continue

                answer[i] = True

            if sum(answer[left-1:right]) == right-left+1:
                return True
        
        return False
