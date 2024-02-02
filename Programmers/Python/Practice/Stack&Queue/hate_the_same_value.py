def solution(arr):
    answer = []
    previous_value = arr[0]
    answer.append(previous_value)

    for _arr in arr[1:]:
        if _arr != previous_value:
            answer.append(_arr)

        previous_value = _arr
    
    return answer
