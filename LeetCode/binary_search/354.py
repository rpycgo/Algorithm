class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = []

        for _, h in envelopes:
            if not tails or tails[-1] < h:
                tails.append(h)
            else:
                idx = bisect_left(tails, h)
                tails[idx] = h

        answer = len(tails)

        return answer
