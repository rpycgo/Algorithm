class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answer = [
            [pixel ^ 1 for pixel in reversed(row)]
            for row
            in image]

        return answer
