class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if(len(str) == 0):
            return True
        for character in s:
            if(character == '(' or character == '{' or character == '['):
                stack.append(character)
            else:
                if(character == ')' and stack[-1] == '('):
                    stack.pop()
                elif(character == '}' and stack[-1] == '{'):
                    stack.pop()
                elif(character == ']' and stack[-1] == '['):
                    stack.pop()
        
        if(len(stack) == 0):
            return True
        else:
            return False
        