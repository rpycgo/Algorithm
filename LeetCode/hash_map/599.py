class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: i for i, name in enumerate(list2)}
        min_index_sum = float('inf')
        result = []

        for i, name in enumerate(list1):
            if name in index_map:
                total = i + index_map[name]

                if total < min_index_sum:
                    min_index_sum = total
                    result = [name]
                elif total == min_index_sum:
                    result.append(name)

        return result
