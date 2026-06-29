class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for character in s:
            if(character == '(' or character == '{' or character == '['):
                stack.append(character)
            else:
                if(len(stack) > 0):
                    if(character == ')'):
                        if(stack[-1] == '('):
                            stack.pop()
                        else:
                            return False
                    elif(character == '}'):
                        if(stack[-1] == '{'):
                            stack.pop()
                        else:
                            return False
                    elif(character == ']'):
                        if (stack[-1] == '['):
                            stack.pop()
                        else:
                            return False
                else:
                    return False
        
        if(len(stack) == 0):
            return True
        else:
            return False
        