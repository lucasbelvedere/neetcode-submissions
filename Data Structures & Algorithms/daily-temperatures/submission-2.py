class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonicStack = [] # decreasing monotonic stack
        outputs = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while (len(monotonicStack) != 0) and (temperatures[i] > temperatures[monotonicStack[len(monotonicStack) - 1]]):
                index = monotonicStack.pop()
                outputs[index] = i - index
            monotonicStack.append(i)
        return outputs