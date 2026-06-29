# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        def dfs(root, answer):
            if not root:
                return
            
            print(root.val)
            answer.append(root.val)
            if root.right:
                dfs(root.right, answer)
            elif root.left:
                dfs(root.left, answer)
            return answer
        
        answer = dfs(root, [])

        return answer if answer else []