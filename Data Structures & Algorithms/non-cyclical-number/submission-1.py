class Solution:
    def isHappy(self, n: int) -> bool:

        def number_to_arr(number):
            res = []

            while number:
                res.append(number % 10)
                number = number // 10
            
            return res
        
        seen = set()

        curr_list = number_to_arr(n)

        

        while True:
            squared = [n**2 for n in curr_list]

            squared_sum = sum(squared)
            
            if squared_sum == 1:
                return True
            elif squared_sum in seen:
                return False
            
            curr_list = number_to_arr(squared_sum)
            seen.add(squared_sum)

