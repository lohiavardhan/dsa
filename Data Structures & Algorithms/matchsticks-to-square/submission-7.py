class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        length = sum(matchsticks) / 4
        visited = [False for _ in range(len(matchsticks))]

        def backtrack(i, rem_sides, curr_sum):
            print(i, rem_sides, curr_sum)
            if rem_sides == 0:
                return True
            if curr_sum == length:
                return backtrack(0, rem_sides - 1, 0)
            
            for j in range(i, len(matchsticks)):
                if visited[j] or curr_sum + matchsticks[j] > length:
                    continue
                
                visited[j] = True
                if backtrack(j + 1, rem_sides, curr_sum + matchsticks[j]):
                    return True
                visited[j] = False
            
            return False
        
        return backtrack(0, 4, 0)
