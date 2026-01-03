class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_count = max(counts)
        max_count_tasks = counts.count(max_count)

        part_count = max_count - 1
        part_length = n + 1
        empty_slots = part_count * part_length
        slots_with_tasks = max_count_tasks
        intervals = empty_slots + slots_with_tasks

        answer = max(intervals, len(tasks))

        return answer
