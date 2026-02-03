class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        choices = ('A', 'C', 'G', 'T')
        n = len(startGene)

        visited = set(startGene)

        queue = deque([(startGene, 0)])
        while queue:
            curr_gene, curr_cnt = queue.popleft()

            next_cnt = curr_cnt + 1

            for choice in choices:
                for i in range(n):
                    next_gene = curr_gene[:i] + choice + curr_gene[i+1:]

                    if next_gene == endGene:
                        return next_cnt

                    if next_cnt < 10 and next_gene in bank and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, next_cnt))

        return -1
