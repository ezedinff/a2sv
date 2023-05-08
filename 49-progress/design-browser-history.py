from collections import deque

class BrowserHistory:

    def __init__(self, homepage: str):
        # self.history = [homepage]
        # self.curr = 0
        self.history = deque([homepage])
        self.curr = 0

    def visit(self, url: str) -> None:
        # self.history = self.history[:self.curr + 1]
        # self.history.append(url)
        # self.curr += 1
        while len(self.history) > self.curr + 1:
            self.history.pop()
        self.history.append(url)
        self.curr += 1
        

    def back(self, steps: int) -> str:
        # self.curr = max(0, self.curr - steps)
        # return self.history[self.curr]
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]
        

    def forward(self, steps: int) -> str:
        # self.curr = min(len(self.history) - 1, self.curr + steps)
        # return self.history[self.curr]
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)