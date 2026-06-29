class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_preqreq = defaultdict(list)

        for curr, req in prerequisites:
            course_preqreq[req].append(curr)

        for curr, req in prerequisites:
            if curr in course_preqreq[req] and req in course_preqreq[curr]:
                return False
        
        # for i in range(numCourses):
        #     if i not in visited:
        #         return False
            
        return True