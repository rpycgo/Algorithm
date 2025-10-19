from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        skip = 0
        while students and skip < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()

                skip = 0
            else:
                students.append(students.popleft())

                skip += 1

        return len(students)
