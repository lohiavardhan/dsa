# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = {}
        
        def dfs(node, depth):
            nonlocal answer
            if not node:
                return 
            
            if depth in answer:
                answer[depth].append(node.val)
            else:
                answer[depth] = [node.val] 

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        return list(answer.values())