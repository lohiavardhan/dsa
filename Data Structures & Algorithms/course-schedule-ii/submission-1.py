class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hashmap = {}

        for i in range(numCourses):
            hashmap[i] = []
        
        for course, pre in prerequisites:
            hashmap[course].append(pre)
        
        res = set()
        def dfs(curr_num, visited):
            nonlocal res
            if curr_num in visited:
                return False
            if hashmap[curr_num] == []:
                res.add(curr_num)
                return True
            
            visited.add(curr_num)
            for pre in hashmap[curr_num]:
                if not dfs(pre, visited):
                    res = []
                    return False
            
            hashmap[curr_num] = []
            res.add(curr_num)
            return True
        
        for course, _ in prerequisites:
            if not dfs(course, set()):
                return []
        
        for i in range(numCourses):
            if i not in res:
                res.add(i)
        
        return list(res)