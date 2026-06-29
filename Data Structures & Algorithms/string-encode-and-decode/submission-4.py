class Solution:

    def encode(self, strs: List[str]) -> str:
        return "||".join(strs)
    def decode(self, s: str) -> List[str]:
       
        if s == "" or s == '':
            return [""]
        return s.split("||")
