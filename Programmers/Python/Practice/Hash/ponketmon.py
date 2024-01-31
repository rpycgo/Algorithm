def solution(nums):
    result = {}
    
    for num in nums:
        if (answer := len(result)) >= len(nums)//2:
            break

        if num not in result:
            result[num] = 0

        result[num] += 1

    
    return answer