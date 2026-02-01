class RideSharingSystem:

    def __init__(self):
        self.riders = deque([])
        self.drivers = deque([])

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.riders and self.drivers:
            driver_idx = self.drivers.popleft()
            rider_idx = self.riders.popleft()

            return [driver_idx, rider_idx]

        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.riders:
            self.riders.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)©leetcode