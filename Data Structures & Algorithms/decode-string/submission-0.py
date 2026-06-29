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
                stack[-1] = int(stack[-1]) * string
            else:
                stack.append(s[i])
        

        return "".join(stack)