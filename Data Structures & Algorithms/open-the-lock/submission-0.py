class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)
        q = collections.deque()
        q.append(['0000', 0])
        i = 0
        visited = set()
        while q:
            
            curr_num, steps = q.popleft()
            #print(q, curr_num, steps)
            
            if curr_num in dead or curr_num in visited:
                continue
            if curr_num == target:
                return steps
            
            visited.add(curr_num)
            curr_num_list = list(curr_num)
            new_list = curr_num_list.copy()
            
            for i in range(len(curr_num_list)):
                
                number = int(curr_num_list[i])
                
                if number == 0:
                    new_plus = 1
                    new_minus = 9
                elif number == 9:
                    new_plus = 0
                    new_minus = 8
                else:
                    new_plus = number + 1
                    new_minus = number - 1
                
                
                temp = new_list[i]
                new_list[i] = str(new_plus)
                new_num = "".join(new_list)
                q.append([new_num, steps + 1])
                #print(new_num)
                
                new_list[i] = str(new_minus)
                new_num = "".join(new_list)
                q.append([new_num, steps + 1])
                #print(new_num)
                new_list[i] = temp
                

        return -1


