class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        curr_list = []
        
        while n:
            curr_list.append(n % 10)
            n = n // 10


        while True:
            squared = [n**2 for n in curr_list]

            squared_sum = sum(squared)
            
            if squared_sum == 1:
                return True
            elif squared_sum in seen:
                return False
            
            curr_list = squared
            seen.add(squared_sum)

