class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        distinct_candy_types = len(set(candyType))
        doctor_allowed_candies = len(candyType) // 2

        answer = min(distinct_candy_types, doctor_allowed_candies)

        return answer
