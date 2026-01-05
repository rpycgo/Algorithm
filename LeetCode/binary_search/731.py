class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []


    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect_left(self.overlaps, (endTime, 0))

        for start, end in self.overlaps[:idx]:
            if startTime < end and start < endTime:
                return False

        for start, end in self.calendar:
            if startTime < end and start < endTime:
                new_overlap = (max(start, startTime), min(end, endTime))
                insort(self.overlaps, new_overlap)

        self.calendar.append((startTime, endTime))

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)