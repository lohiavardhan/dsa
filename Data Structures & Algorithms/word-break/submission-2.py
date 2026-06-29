class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        start_index = 0
        checker = True

        if(len(s) == 1):
            if(s in wordDict):
                return True
            else:
                return False
        
        while start_index < len(s):
            temp = start_index
            for end_index in range(start_index + 1, len(s)):
                if(s[start_index:end_index + 1] in wordDict):
                    print(s[start_index: end_index + 1])
                    start_index = end_index + 1

                    if(start_index >= len(s)):
                        return True
                    break
                
            
            if(start_index == temp):
                return False
        
        return True

        