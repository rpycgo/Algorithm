class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        counter = Counter(ages)

        answer = 0
        for age in counter.keys():
            if age < 15:
                continue

            lower_bound = int(age*0.5 + 7) + 1

            idx_left = bisect_left(ages, lower_bound)
            idx_right = bisect_right(ages, age)

            count = idx_right - idx_left

            if count > 0:
                answer += (counter[age] * (count-1))

        return answer
