class NumArray:
    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.nums = nums

        self.h = self.N.bit_length()
        self.size = 1 << self.h

        self.tree = [0] * (self.size * 2)

        self._build()

    def _build(self):
        for i, val in enumerate(self.nums):
            self.tree[self.size + i] = val

        for i in range(self.size-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]

    def update(self, index: int, val: int) -> None:
        idx = self.size + index
        self.tree[idx] = val

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[idx*2] + self.tree[idx*2 + 1]

    def sumRange(self, left: int, right: int) -> int:
        left += self.size
        right += self.size

        total = 0
        while left <= right:
            if left%2 == 1:
                total += self.tree[left]
                left += 1

            if right%2 == 0:
                total += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return total

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)