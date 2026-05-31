class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # two
        numStack = []
        for c in tokens:
            if c == "+":
                numStack.append(numStack.pop() + numStack.pop())
            elif c == "-":
                b, a = numStack.pop(), numStack.pop()
                numStack.append((a - b))
            elif c == "*":
                numStack.append(numStack.pop() * numStack.pop())
            elif c == "/":
                b, a = numStack.pop(), numStack.pop()
                numStack.append(int(a / b))
            else:
                numStack.append(int(c))
                
        return numStack.pop()

        