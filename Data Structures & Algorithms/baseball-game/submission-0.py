class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreStack = []
        for operation in operations:
            if operation == "C":
                scoreStack.pop()
            elif operation == "D":
                a = scoreStack.pop()
                scoreStack.append(a)
                scoreStack.append(a * 2)
            elif operation == "+":
                b, a = scoreStack.pop(), scoreStack.pop()
                scoreStack.append(a)
                scoreStack.append(b)
                scoreStack.append(a + b)
            else:
                scoreStack.append(int(operation))
            print(scoreStack)

        return sum(scoreStack)

        