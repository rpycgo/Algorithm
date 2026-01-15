import sys


input = sys.stdin.readline


class Factory:
    def __init__(self, N, target):
        self.N = N
        self.arr = target

        self.answer = 0

    def merge_sort(self, start, end):
        if start < end:
            mid = (start+end) // 2

            self.merge_sort(start, mid)
            self.merge_sort(mid+1, end)
            self.sort(start, mid, end)

    def sort(self, start, mid, end):
        temp = []
        i = start
        j = mid + 1

        while i <= mid and j <= end:
            if self.arr[i] < self.arr[j]:
                temp.append(self.arr[i])
                i += 1
            else:
                temp.append(self.arr[j])
                j += 1

                self.answer += (mid - i + 1)

        while i <= mid:
            temp.append(self.arr[i])
            i += 1

        while j <= end:
            temp.append(self.arr[j])
            j += 1

        for k, val in enumerate(temp):
            self.arr[start+k] = val

    def run(self):
        self.merge_sort(0, self.N - 1)

        print(self.answer)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    pos_b = {val: i for i, val in enumerate(B)}
    target = [pos_b[x] for x in A]

    Factory(N, target).run()
