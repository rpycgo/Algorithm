import sys

input = sys.stdin.readline


def main():
    while True:
        line = input().rstrip()
        if line == '#':
            break

        stack = []
        is_error = False

        i = 0
        while i < len(line):
            if line[i] == '<':
                end_idx = line.find('>', i)
                tag_content = line[i+1:end_idx]

                if tag_content.endswith('/'):
                    pass
                elif tag_content.startswith('/'):
                    tag_name = tag_content[1:]

                    if not stack or stack[-1] != tag_name:
                        is_error = True
                        break

                    stack.pop()
                else:
                    tag_name =  tag_content.split()[0]
                    stack.append(tag_name)

                i = end_idx
            i += 1

        answer = 'legal' if not is_error and not stack else 'illegal'
        print(answer)


if __name__ == '__main__':
    main()
