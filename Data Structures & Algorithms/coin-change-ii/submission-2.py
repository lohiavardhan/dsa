class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if amount == 0:
            return 1
        
        memo = {}
        res = 0
        already_counted = set()
        used = [0 for _ in range(len(coins))]

        def dfs(target):
            nonlocal res
            if target == amount and tuple(used) not in already_counted:
                already_counted.add(tuple(used))
                return True
            if target > amount:
                return False
            

            for c in range(len(coins)):
                used[c] += 1
                if dfs(target + coins[c]):
                    res += 1
                used[c] -= 1

                memo[target] = res
            return False
        
        dfs(0)
        print(res)
        return res