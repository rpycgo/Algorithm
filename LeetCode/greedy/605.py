class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) == 1 and n == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False

        n_left = n
        i = 1

        if sum(flowerbed[:2]) == 0:
            flowerbed[0] = 1
            n_left -= 1

        if sum(flowerbed[-2:]) == 0 and n_left >= 1:
            flowerbed[-1] = 1
            n_left -= 1

        while (n_left != 0) and (i != len(flowerbed)-1):
            if sum(flowerbed[i-1:i+2]) == 0:
                flowerbed[i] = 1
                n_left -= 1

            i += 1

        result = False if n_left else True

        return result
