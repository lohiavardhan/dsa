class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        prev = [0 for _ in range(amount + 1)]
        curr = [0 for _ in range(amount + 1)]
        prev[-1] = 1
        curr[-1] = 1

        for c in coins:
            
            for a in range(amount, -1, -1):
                if a + c <= amount:
                    curr[a] = prev[a] + curr[a + c]
            
            #print(f'{c=}, {prev=}, {curr=}')
            prev = curr
            
        return curr[0]


        
