class Solution:
    def isValid(self, s: str) -> bool:

        stack = collections.deque()

        openings = set(['(', '[', '{'])
        print('(' in openings)

        for char in s:
            if char in openings:
                stack.append(char)
            else:
                curr_bracket = stack.pop()
                if  (char == ')' and curr_bracket != '(') or (char == '}' and curr_bracket != '{') or (char == ']' and curr_bracket != '['):
                    return False

        return True if len(stack) == 0 else False

        