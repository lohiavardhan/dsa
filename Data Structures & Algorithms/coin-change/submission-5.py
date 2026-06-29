class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        answer = [float("inf") for _ in range(amount + 1)]
        answer[0] = 0
        for c in coins:
            if c >= len(answer):
                continue
            answer[c] = 1
        
        for i in range(amount + 1):
            for c in coins:
                
                if (i - c) >= 0:
                    answer[i] = min(answer[i - c] + 1, answer[i])


        print(answer)

        if answer[-1] == float("inf"):
            return -1
        
        return answer[-1]