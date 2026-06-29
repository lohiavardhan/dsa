class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            
            w1 = words[i]
            w2 = words[i+1]
            minimum = min(len(w1), len(w2))

            if len(w2) < len(w1) and w1[:minimum] == w2[:minimum]:
                return ""
            
            for c in range(minimum):
                if w1[c] != w2[c]:
                    adj[w1[c]].add(w2[c])
                    break
            
        visited = set()
        res = []
        print(adj)

        def dfs(char):
            if adj[char] == "":
                return True
            if char in visited:
                return False
            
            visited.add(char)

            for next_c in adj[char]:
                if not dfs(next_c):
                    return False
            
            adj[char] = ""
            res.append(char)
            visited.remove(char)

            return True
        
        for chars in adj:
            if not dfs(chars):
                return ""
        
        res.reverse()
        return "".join(res)