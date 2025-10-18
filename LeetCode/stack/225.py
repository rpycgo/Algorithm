class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.queue:
            return False

        pop_value = self.queue[-1]

        self.queue = self.queue[:len(self.queue)-1]

        return pop_value

    def top(self) -> int:
        if not self.queue:
            return False

        return self.queue[-1]

    def empty(self) -> bool:
        return True if not self.queue else False
