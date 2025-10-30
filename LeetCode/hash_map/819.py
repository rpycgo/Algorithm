class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        paragraph = paragraph.lower()
        paragraph = paragraph.replace('!', '').replace('?', '')\
            .replace("'", '').replace(';', '').replace('.', ' ').replace(',', ' ')

        count = defaultdict(int)
        for word in paragraph.split():
            print(word)
            if word not in banned:
                count[word] += 1

        return max(count, key=count.get)
