class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect_left(self.intervals, (startTime, endTime))

        if idx > 0 and self.intervals[idx-1][1] > startTime:
            return False

        if idx < len(self.intervals) and self.intervals[idx][0] < endTime:
            return False

        self.intervals.insert(idx, (startTime, endTime))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)