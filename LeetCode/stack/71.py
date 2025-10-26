class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_split = path.split('/')
        for path in path_split:
            if path == '..':
                if not stack:
                    stack.append('')
                else:
                    stack.pop()
            elif not path or path == '.':
                continue
            else:
                stack.append(path)

        if not stack:
            stack.append('')

        answer = '/'.join(stack)
        if not answer or answer[0] != '/':
            answer = '/' + answer

        return answer
