class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = defaultdict(list)

        for i, num in enumerate(nums):
            hash_map[num].append(i)

        hash_map_w_least_2_values = {
            key: value
            for key, value
            in hash_map.items()
            if len(value) >= 2
        }

        for value in hash_map_w_least_2_values.values():
            n = len(value)
            for i in range(n):
                for j in range(i+1, n):
                    if abs(value[i]-value[j]) <= k:
                        return True

        return False
