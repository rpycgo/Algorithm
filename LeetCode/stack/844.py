class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for char_s in s:
            if char_s != '#':
                stack_s.append(char_s)
            elif char_s == '#' and stack_s:
                stack_s.pop()
        
        for char_t in t:
            if char_t != '#':
                stack_t.append(char_t)
            elif char_t == '#' and stack_t:
                stack_t.pop()
        
        return True if stack_s == stack_t else False
