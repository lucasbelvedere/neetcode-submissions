class MinStack:

    def __init__(self):
        # we can define stacks with lists in python
        self.stack = []
        self.minValueStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        minValue = min(val, self.minValueStack[len(self.minValueStack) - 1]) if len(self.minValueStack) > 0 else val
        self.minValueStack.append(minValue)
        

    def pop(self) -> None:
        if len(self.stack) != 0: # both lists will always have the same len
            self.stack.pop()
            self.minValueStack.pop()

        
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        return 0
        

    def getMin(self) -> int:
        if len(self.minValueStack) > 0:
            return self.minValueStack[len(self.minValueStack) - 1]
        return 0
        
