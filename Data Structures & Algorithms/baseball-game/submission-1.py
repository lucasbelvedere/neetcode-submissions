class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []
        for operation in operations:
            if operation == "C":
                scoreStack.pop()
            elif operation == "D":
                scoreStack.append(scoreStack[-1] * 2)
            elif operation == "+":
                b, a = scoreStack[-1], scoreStack[-2]
                scoreStack.append(a + b)
            else:
                scoreStack.append(int(operation))

        return sum(scoreStack)

        