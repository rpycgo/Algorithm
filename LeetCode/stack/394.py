class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        char_stack = []
        current_string = ''
        num = 0

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                num_stack.append(num)
                char_stack.append(current_string)
                current_string = ''
                num = 0
            elif char == ']':
                repeat = num_stack.pop()
                prev_string = char_stack.pop()
                current_string = prev_string + current_string*repeat
            else:
                current_string += char

        return current_string
