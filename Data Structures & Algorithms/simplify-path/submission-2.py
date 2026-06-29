class Solution:
    def simplifyPath(self, path: str) -> str:
        divided = path.split('/')
        answer = ''
        stack = []
        

        for curr_item in divided:
            if curr_item == "..":
                if stack:
                    stack.pop()
            elif curr_item != "" and curr_item != ".":
                stack.append(curr_item)


        return '/' + '/'.join(stack)