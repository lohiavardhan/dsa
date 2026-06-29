class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def backtrack(i, total):
            if(total == target):
                test = subset.copy()
                test.sort()
                if test not in res:
                    res.append(test.copy())
                return
            
            if(total > target or i >= len(candidates)):
                return
            
            subset.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            subset.pop()
            backtrack(i + 1, total)

        
        backtrack(0, 0)
        return res

        