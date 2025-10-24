class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        answer = []
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')

        for word in words:
            count = {
                'first_row': 0,
                'second_row': 0,
                'third_row': 0,
            }

            for char in word:
                char = char.lower()

                if char in first_row:
                    count['first_row'] += 1
                elif char in second_row:
                    count['second_row'] += 1
                else:
                    count['third_row'] += 1

            values = [key for key, value in count.items() if value > 0]

            if len(values) == 1:
                answer.append(word)

        return answer
