class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()

        for curr, req in prerequisites:
            
            if req in visited:
                return False
            
            visited.add(curr)
        
        # for i in range(numCourses):
        #     if i not in visited:
        #         return False
            
        return True