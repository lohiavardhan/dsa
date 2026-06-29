class Solution:
    def simplifyPath(self, path: str) -> str:
        divided = path.split('/')
        answer = ''
        stack = []
        

        for curr_item in divided:
            print(stack, curr_item)
            if len(curr_item) == 0:
                continue
            
            if curr_item[0] == '.':
                if len(curr_item) == 1:
                    continue
                if len(curr_item) % 2 == 0:
                    if stack:
                        _ = stack.pop()
                    else:
                        continue
                else:
                    stack.append('.')
            else:
                stack.append(curr_item)

        print(stack)

        return '/' + '/'.join(stack)