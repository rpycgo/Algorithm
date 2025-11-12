class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        match_count = 0

        for char in s:
            while i < len(t) and match_count != len(s):
                if t[i] == char:
                    match_count += 1
                    i += 1

                    break
                else:
                    i += 1

            if match_count == len(s):
                return True

        return False
