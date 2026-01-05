class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_frequencies = [0] * 121
        for age in ages:
            age_frequencies[age] += 1

        prefix = [0] * 122
        for i, age_frequency in enumerate(age_frequencies, start=1):
            prefix[i] = prefix[i-1] + age_frequency

        answer = 0
        for age in range(15, 121):
            if age_frequencies[age] == 0:
                continue

            low_bound = int(age*0.5+7) + 1

            if low_bound > age:
                continue

            count = prefix[age+1] - prefix[low_bound]
            answer += age_frequencies[age] * (count-1)

        return answer
