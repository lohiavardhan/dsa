class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {c: set() for w in words for c in w}
        print(adj)
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minimum = min(len(w1), len(w2))
            checker = 0

            for j in range(minimum):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    checker = 1
                    break
            
            
            if checker == 0:
                return ""
        
        print(adj)
        visited = set()
        answer = []

        def dfs(curr_str):
            if adj[curr_str] == '':
                return True
            if curr_str in visited:
                return False
            
            visited.add(curr_str)
            

            for next_c in adj[curr_str]:
                if not dfs(next_c):
                    return False
            
            adj[curr_str] = ''
            visited.remove(curr_str)
            
            answer.append(curr_str)
            return True
        
        
        for char in adj:
            if not dfs(char):
                return ""
        
        answer.reverse()

        return "".join(answer)
                
            
            

