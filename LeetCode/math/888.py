class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_b-sum_a) // 2
        set_b = set(bobSizes)

        for alice_size in aliceSizes:
            y = alice_size + diff

            if y in set_b:
                return [alice_size, y]
