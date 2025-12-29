class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map1 = defaultdict(int)
        hash_map2 = defaultdict(int)

        for num in nums1:
            hash_map1[num] += 1
        for num in nums2:
            hash_map2[num] += 1

        common_keys = hash_map1.keys() & hash_map2.keys()
        min_values_by_key = [min(hash_map1[key], hash_map2[key]) for key in common_keys]

        answer = []
        for common_key, min_value_by_key in zip(common_keys, min_values_by_key):
            answer.extend([common_key] * min_value_by_key)

        return answer
