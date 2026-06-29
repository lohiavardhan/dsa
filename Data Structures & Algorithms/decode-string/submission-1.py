class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == ']':
                string = ''
                while stack[-1] != '[':
                    curr_char = stack.pop()
                    string += curr_char
                string = string[::-1]
                _ = stack.pop()
                number = ''

                while stack and stack[-1].isdigit():
                    number += stack.pop()
                number = number[::-1]
                number = int(number)
                stack.append(number * string)

            else:
                stack.append(s[i])
        

        return "".join(stack)