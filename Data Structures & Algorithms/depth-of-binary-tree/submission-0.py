# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        answer = 0
        answer = max(answer, 1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

        return answer