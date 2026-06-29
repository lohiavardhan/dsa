class Solution:
    def isPalindrome(self, s: str) -> bool:

        

        string = "".join(filter(str.isalnum, s)).lower()


        l = 0
        r = len(string) - 1

        while l <= r:
            if string[l] != string[r]:
                print(l, r, string[l], string[r])
                return False
            
            l += 1
            r -= 1
        
        return True
        