class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashmap = {}

        for i in range(numCourses):
            hashmap[i] = []

        for curr, prereq in prerequisites:
            hashmap[curr].append(prereq)
        

        def dfs(curr_set, curr_num):
            if len(hashmap[curr_num]) == 0:
                return True
            if curr_num in curr_set:
                return False
            
            curr_set.add(curr_num)
            for next_num in hashmap[curr_num]:
                if not dfs(curr_set, next_num):
                    return False
                else:
                    hashmap[curr_num].remove(next_num)
            curr_set.remove(curr_num)

            return True
        
        for i in range(numCourses):
            if not dfs(set(), i):
                return False

        print(hashmap)
        return True