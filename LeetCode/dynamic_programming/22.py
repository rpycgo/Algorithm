class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
    
        self.backtrack(answer, '', n, n)

        return answer

    def backtrack(self, parenthesis, s, left, right):
        if left == 0 and right == 0:
            parenthesis.append(s)

            return
        
        if left > 0:
            self.backtrack(parenthesis, s + '(', left-1, right)
        
        if right > left:
            self.backtrack(parenthesis, s + ')', left, right-1)
