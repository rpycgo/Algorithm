class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_split = path.split('/')
        for path in path_split:
            if path == '..':
                if stack:
                    stack.pop()
            elif not path or path == '.':
                continue
            else:
                stack.append(path)

        answer = '/' + '/'.join(stack)

        return answer
