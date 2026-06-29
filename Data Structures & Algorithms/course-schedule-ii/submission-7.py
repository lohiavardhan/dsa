class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        hashmap = {}
        added = [False for _ in range(numCourses)]
        for i in range(numCourses):
            hashmap[i] = []
        
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        def dfs(curr_num, visited):
            nonlocal res
            if hashmap[curr_num] == []:
                if not added[curr_num]:
                    res.append(curr_num)
                    added[curr_num] = True
            if curr_num in visited:
                return False
            
            visited.add(curr_num)
            for pre in hashmap[curr_num]:
                if not dfs(pre, visited):
                    return False
            visited.remove(curr_num)
            hashmap[curr_num] = []
            
            if not added[curr_num]:
                res.append(curr_num)
                added[curr_num] = True
            
            return True
        
        
        for i in range(numCourses):
            if added[i]:
                continue
            if not dfs(i, set()):
                return []
        
        return res
        