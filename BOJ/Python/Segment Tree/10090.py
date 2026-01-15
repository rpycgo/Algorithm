import sys


input = sys.stdin.readline


class InversionCount:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

        self.answer = 0

    def merge_sort(self, start, end):
        if start < end:
            mid = (start+end) // 2

            self.merge_sort(start, mid)
            self.merge_sort(mid+1, end)
            self.merge(start, mid, end)

    def merge(self, start, mid, end):
        temp = []
        i, j = start, mid + 1

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
        self.merge_sort(0, self.n-1)

        print(self.answer)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    InversionCount(n, arr).run()
