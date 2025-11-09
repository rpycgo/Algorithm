class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        in_stack = set()
        stack = []

        for char in s:
            count[char] -= 1

            if char in in_stack:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(char)
            in_stack.add(char)

        answer = ''.join(stack)

        return answer
