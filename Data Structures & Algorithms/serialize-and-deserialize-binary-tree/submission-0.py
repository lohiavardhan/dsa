# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        data = ''

        def inorder(node):
            nonlocal data
            if not node:
                return 
            
            inorder(node.left)
            data += '_' + str(node.val)
            inorder(node.right)
        
        inorder(root)

        data += '++'
        
        def preorder(node):
            nonlocal data
            if not node:
                return
            data += '_' + str(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        print(data)
        return data

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        both = data.split('++')
        print(both)
        inorder = list(map(int, both[0].split('_')[1:]))
        preorder = list(map(int, both[1].split('_')[1:]))
        
        def backtrack(inorder, preorder):
            if not inorder:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = backtrack(inorder[:mid], preorder[1:mid + 1])
            root.right = backtrack(inorder[mid + 1:], preorder[mid + 1:])

            return root

        return backtrack(inorder, preorder)
