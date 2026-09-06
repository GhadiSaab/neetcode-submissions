class MinStack:

    def __init__(self):
        self.list = []
        self.mini = []
        
        

    def push(self, val: int) -> None:
        self.list.append(val)
        min_val = min(val, self.mini[-1]) if self.mini else val
        self.mini.append(min_val)

    def pop(self) -> None:
        self.list = self.list[:-1]
        self.mini = self.mini[:-1]

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
