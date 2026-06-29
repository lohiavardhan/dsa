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
        
        visited = set()
        answer = []

        def dfs(curr_char):
            if adj[curr_char] == "":
                return True
            if curr_char in visited:
                return False
            
            visited.add(curr_char)
            for next_char in adj[curr_char]:
                if not dfs(next_char):
                    return False
                
            adj[curr_char] = ""
            answer.append(curr_char)
            visited.remove(curr_char)

            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        
        answer.reverse()
        return "".join(answer)