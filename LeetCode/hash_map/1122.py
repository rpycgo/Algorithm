class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in arr1:
            count[num] += 1

        answer = []
        for num in arr2:
            answer.extend([num]*count[num])

        arr2_set = set(arr2)
        elem_not_in_arr2 = []
        for num in arr1:
            if num not in arr2_set:
                elem_not_in_arr2.append(num)
        elem_not_in_arr2.sort()

        answer = answer + elem_not_in_arr2

        return answer
