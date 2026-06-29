class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        list_str = [str(s) for s in digits]

        number_str = "".join(list_str)
        number_int = int(number_str)
        number_int += 1
        number_str = str(number_int)
        
        return_list = list(number_str)

        return_l = [int(n) for n in return_list]

        return return_l