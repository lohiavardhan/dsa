class Solution:
    def reverseBits(self, n: int) -> int:
        num = ''
        for i in range(32):
            if n % 2:
                num = num + '1'
            else:
                num = num + '0'
            
            n = n >> 1
        
        return int(num, 2)