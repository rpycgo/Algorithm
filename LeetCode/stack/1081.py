class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = Counter(s)
        in_stack = set()
        stack = []

        for char in s:
            count[char] -= 1

            if char in in_stack:
                continue

            while stack and count[stack[-1]] and char < stack[-1]:
                removed = stack.pop()
                in_stack.remove(removed)

            in_stack.add(char)
            stack.append(char)

        answer = ''.join(stack)

        return answer
