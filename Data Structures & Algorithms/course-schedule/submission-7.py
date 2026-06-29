class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for c1, c2 in prerequisites:
            adj[c1].append(c2)
        
        visited = set()

        def dfs(curr_num):
            if adj[curr_num] == []:
                return True
            if curr_num in visited:
                return False
            
            visited.add(curr_num)

            for prereq in adj[curr_num]:
                if not dfs(prereq):
                    return False
            
            adj[curr_num] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False


        return True