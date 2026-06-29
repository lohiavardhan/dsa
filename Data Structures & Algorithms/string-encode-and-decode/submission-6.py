class Solution:

    def encode(self, strs: List[str]) -> str:

        ret = ""

        for word in strs:
            count = len(word)

            print(count, word)
            ret += str(count)
            ret += word
        
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:

        ret = []

        i = 0
        
        while(i < len(s)):
            count = int(s[i])
            temp = i + 1
            i += count + 1

            ret.append(s[temp:i])
        
            print(ret, i, temp, s[temp:])
        return ret
