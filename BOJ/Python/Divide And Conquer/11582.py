import sys


input = sys.stdin.readline



class ChickenTopN:
    def __init__(self, N, k, arr):
        self.N = N
        self.k = k
        self.arr = arr

    def _divide(self):
        step = self.N // self.k

        answer = []
        for i in range(0, self.N, step):
            part = self.arr[i:i+step]
            part.sort()
            answer.extend(part)

        return answer

    def run(self):
        answer = self._divide()
        print(*answer)



if __name__ == '__main__':
    N = int(input())
    scores = list(map(int, input().split()))
    k = int(input())

    chicken_top_n = ChickenTopN(N, k, scores)
    chicken_top_n.run()
