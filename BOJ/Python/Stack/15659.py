import sys


input = sys.stdin.readline


class OperationInsertion:
    def __init__(self, N, A, n_operations):
        self.N = N
        self.A = A
        self.n_operations = n_operations

        self.max_val = float('-inf')
        self.min_val = float('inf')

    def calculate(self, curr_operation):
        num_stack = [self.A[0]]
        for i in range(self.N-1):
            operator = curr_operation[i]
            next_num = self.A[i+1]

            if operator == 0:
                num_stack.append(next_num)
            elif operator == 1:
                num_stack.append(-next_num)
            elif operator == 2:
                prev_num = num_stack.pop()
                num_stack.append(prev_num * next_num)
            elif operator == 3:
                prev_num = num_stack.pop()

                if prev_num < 0:
                    num_stack.append(-(-prev_num // next_num))
                else:
                    num_stack.append(prev_num // next_num)

        return sum(num_stack)

    def dfs(self, depth, curr_operation):
        if depth == self.N-1:
            result = self.calculate(curr_operation)
            self.max_val = max(self.max_val, result)
            self.min_val = min(self.min_val, result)
            return

        for i in range(4):
            if self.n_operations[i] > 0:
                self.n_operations[i] -= 1
                curr_operation.append(i)

                self.dfs(depth+1, curr_operation)

                curr_operation.pop()
                self.n_operations[i] += 1

    def run(self):
        self.dfs(0, [])

        print(self.max_val)
        print(self.min_val)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    n_operators = list(map(int, input().split()))

    operation_insertion = OperationInsertion(N, A, n_operators)
    operation_insertion.run()
