def solution(s):
    if s[0] == ')':
        return False
    
    stack = []
    for parenthesis in s:
        if parenthesis == '(':
            stack.append(parenthesis)
        elif parenthesis == ')':
            if len(stack) == 0:
                return False

            stack.pop()
    
    answer = True if len(stack) == 0 else False
    
    return answer