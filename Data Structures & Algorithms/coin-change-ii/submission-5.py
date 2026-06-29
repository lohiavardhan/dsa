class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = [0 for _ in range(amount + 1)]
        memo[-1] = 1

        for c in coins:
            
            new_arr = memo.copy()
            for a in range(amount, -1, -1):
                
                if a + c <= amount:
                    new_arr[a] = memo[a + 1] + memo[a + c]
            memo = new_arr
            #print(f'{c=}, {memo=}')
            
        return memo[0]


        
