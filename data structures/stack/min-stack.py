class MinStack:
    def __init__(self):
        self.items = []
        self.min = []
    def push(self, item):
        self.items.append(item)
        if len(self.min) == 0 or item <= self.min[-1]:
            self.min.append(item)
    def pop(self):
        item = self.items.pop()
        if item == self.min[-1]:
            self.min.pop()
        return item
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def get_min(self):
        return self.min[-1]