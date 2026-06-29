class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            minimum = min(len(w1), len(w2))
            if len(w2) < len(w1) and w1[:minimum] == w2[:minimum]:
                return ""
            
            for j in range(minimum):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = set()
        res = []

        def dfs(char):
            if adj[char] == '':
                return True
            if char in visited:
                return False
            
            visited.add(char)

            for next_char in adj[char]:
                if not dfs(next_char):
                    return False
            
            adj[char] = ''
            visited.remove(char)
            res.append(char)

            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        
        res.reverse()
        return "".join(res)