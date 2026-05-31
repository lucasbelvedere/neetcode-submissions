class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # two
        numStack = []
        for c in tokens:
            if c == "+":
                b = numStack.pop()
                a = numStack.pop()
                numStack.append((a + b))
            elif c == "-":
                b = numStack.pop()
                a = numStack.pop()
                numStack.append((a - b))
            elif c == "*":
                b = numStack.pop()
                a = numStack.pop()
                numStack.append((a * b))
            elif c == "/":
                b = numStack.pop()
                a = numStack.pop()
                numStack.append(int(a / b))
            else:
                numStack.append(int(c))
                
        return numStack.pop()

        