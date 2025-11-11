class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = set(list1) & set(list2)

        min_sum_index = float('inf')
        common_string_with_min_sum_index = ['']
        for common_string in common_strings:
            if list1.index(common_string) + list2.index(common_string) < min_sum_index:
                min_sum_index = list1.index(common_string) + list2.index(common_string)
                common_string_with_min_sum_index[0] = common_string
            elif list1.index(common_string) + list2.index(common_string) == min_sum_index:
                min_sum_index = list1.index(common_string) + list2.index(common_string)
                common_string_with_min_sum_index.append(common_string)

        return common_string_with_min_sum_index
