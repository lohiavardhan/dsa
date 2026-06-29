class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    

class TrieStruct:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.endOfWord = True
    
    def search(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.endOfWord



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieStruct()

        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
            trie.add(word)
        
        res = set()

        def dfs(i, j, curr_string, path):
            if i < 0 or i >= len(board) or j < 0  or j >= len(board[0]) or len(curr_string) > max_len or (i, j) in path:
                return 
            
            curr_string += board[i][j]
            path.add((i, j))
            if trie.search(curr_string) and curr_string not in res:
                res.add(curr_string)

            dfs(i + 1, j, curr_string, path)
            dfs(i - 1, j, curr_string, path)
            dfs(i, j + 1, curr_string, path)
            dfs(i, j - 1, curr_string, path)

            path.remove((i, j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                path = set()
                dfs(i, j, '', path)
            
        return list(res)