class Solution:

    def encode(self, strs: List[str]) -> str:

        ret = ""

        for word in strs:
            count = len(word)

            print(count, word)
            ret += str(count)
            ret += "#"
            ret += word
        
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:

        ret = []

        i = 0
        
        while(i < len(s)):

            count_string = ""
            
            while True:
                if s[i] == "#":
                    break
                else:
                    count_string += s[i]
                    i += 1
            
            count = int(count_string)

            temp = i + 1
            i += count + 1

            ret.append(s[temp:i])
        
            print(ret, i, temp, s[temp:])
        return ret
