# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return 
        
        if p.val < q.val:
            if root.val >= p.val and root.val <= q.val:
                return root
            elif root.val < p.val:
                answer = self.lowestCommonAncestor(root.right, p, q)
                if answer:
                    return answer
            else:
                answer = self.lowestCommonAncestor(root.left, p, q)
                if answer:
                    return answer
        else:
            if root.val <= p.val and root.val >= q.val:
                return root
            elif root.val > p.val:
                answer = self.lowestCommonAncestor(root.left, p, q)
                if answer:
                    return answer
            else:
                answer = self.lowestCommonAncestor(root.right, p, q)
                if answer:
                    return answer
            
