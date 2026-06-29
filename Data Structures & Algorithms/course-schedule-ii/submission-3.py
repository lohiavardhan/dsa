class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = set()
        hashmap = {}
        for i in range(numCourses):
            hashmap[i] = []
        
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        def dfs(curr_num, visited):
            nonlocal res
            if curr_num in visited:
                return False
            
            visited.add(curr_num)
            for pre in hashmap[curr_num]:
                if not dfs(pre, visited):
                    return False
            visited.remove(curr_num)

            if curr_num not in res:
                res.add(curr_num)
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        
        return list(res)
        