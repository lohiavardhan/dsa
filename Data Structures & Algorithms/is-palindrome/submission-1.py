class Solution:
    def isPalindrome(self, s: str) -> bool:

        

        listpal = s.split(' ')
        s = ''.join(listpal)
        s = s.lower()

        s = ''.join(letter for letter in s if letter.isalnum())

        print(s)
        if len(s) % 2 == 0:
            m = len(s) // 2
            l = m - 1
            r = m
        else:
            m = len(s) // 2
            l = m
            r = m

        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                print(s[l], s[r], l, r)
                return False
            
            l -= 1
            r += 1

        return True

        
        