class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        seen = set()

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue

                    a, b, c = digits[i], digits[j], digits[k]

                    if a == 0:
                        continue
                    if c%2 != 0:
                        continue

                    seen.add(a*100 + b*10 + c)

        answer = len(seen)

        return answer
