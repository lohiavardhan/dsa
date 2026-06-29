class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        adj = defaultdict(list)

        for src, dst in tickets:
            adj[src].append(dst)
        
        res = ["JFK"]

        def dfs(city):
            if len(res) == len(tickets) + 1:
                return True
            if city not in adj:
                return False
            
            for i, nxt in enumerate(adj[city]):
                adj[city].pop(i)
                res.append(nxt)
                if dfs(nxt):
                    return True
                adj[city].insert(i, nxt)
                res.pop()
            
            return False
        
        dfs("JFK")

        return res