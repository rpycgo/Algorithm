import sys


input = sys.stdin.readline


class Running:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr

        self.overtake_counts = [0] * N

    def merge_sort(self, start, end):
        if start < end:
            mid = (start+end) // 2

            self.merge_sort(start, mid)
            self.merge_sort(mid+1, end)
            self.sort(start, mid, end)

    def sort(self, start, mid, end):
        temp = []
        i, j = start, mid + 1

        while i <= mid and j <= end:
            if self.arr[i][0] > self.arr[j][0]:
                temp.append(self.arr[i])
                i += 1
            else:
                _, idx = self.arr[j]
                self.overtake_counts[idx] += (mid - i + 1)

                temp.append(self.arr[j])
                j += 1

        while i <= mid:
            temp.append(self.arr[i])
            i += 1

        while j <= end:
            temp.append(self.arr[j])
            j += 1

        for k, val in enumerate(temp):
            self.arr[start+k] = val

    def run(self):
        self.merge_sort(0, self.N-1)

        for i in range(self.N):
            print(i + 1 - self.overtake_counts[i])


if __name__ == '__main__':
    N = int(input())
    arr = [(int(input()), i) for i in range(N)]

    Running(N, arr).run()
