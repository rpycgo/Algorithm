def solution(priorities, location):
    queue = [(i, priority) for i, priority in enumerate(priorities)]

    answer = 0
    while True:
        i, priority = queue.pop(0)
        if any(priority < _priority for _, _priority in queue):
            queue.append((i, priority))
        else:
            answer += 1
            if i == location:
                return answer
