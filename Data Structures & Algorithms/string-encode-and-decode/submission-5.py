class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "1234567809"
        return "||".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "1234567809":
            return []
        if s == "" or s == '':
            return [""]
        return s.split("||")
