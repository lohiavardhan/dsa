class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()

        adj_list = defaultdict(list)

        for src, dest in tickets:
            adj_list[src].append(dest)
        
        res = ["JFK"]

        def dfs(curr_city):
            if len(res) == len(tickets) + 1:
                return True
            if curr_city not in adj_list:
                return False
            
            
            for i, niegh in enumerate(adj_list[curr_city]):
                print(i, niegh, curr_city)
                adj_list[curr_city].pop(i)
                res.append(niegh)
                if dfs(niegh):
                    return True
                adj_list[curr_city].insert(i, niegh)
                res.pop()
            
            return False
            
        dfs("JFK")

        return res