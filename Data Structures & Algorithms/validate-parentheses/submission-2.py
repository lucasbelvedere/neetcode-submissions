class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        openBrackets = {'(', '[', '{'}
        closeBrackets = {')', ']', '}'}

        for char in s:
            print(char)
            if char in openBrackets:
                stack.append(char)
            if char in closeBrackets:
                if len(stack) == 0:
                    return False
                openBracket = stack.pop()
                if (char == ')') and (ord(openBracket) != ord(char) - 1):
                    return False
                elif (char == ']' or char == '}') and (ord(openBracket) != ord(char) - 2):
                    return False

        return True if len(stack) == 0 else False