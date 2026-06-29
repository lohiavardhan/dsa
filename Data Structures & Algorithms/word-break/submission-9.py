class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        answer_array = [False for _ in s]

        for i in range(len(s)):
            for word in wordDict:
                if (i - (len(word) - 1)) >= 0 :
                    if (s[i - (len(word) - 1): i + 1] == word):
                        answer_array[i] = True
                        break
        
        print(answer_array)
        return answer_array[len(s) - 1]

