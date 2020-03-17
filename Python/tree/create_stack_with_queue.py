class Stack:
    queue = []
    top_item = 0

    def push(self, val):
        self.queue.append(val)
        self.top_item = val

    def pop(self) -> int:
        size = len(self.queue)
        while size > 1:
            self.queue.append(self.queue.pop(0))
            size -= 1

        self.top_item = self.queue.pop(0)
        return self.top_item

    def top(self) -> int:
        return self.top_item

    def isEmpty(self) -> bool:
        return len(self.queue) == 0