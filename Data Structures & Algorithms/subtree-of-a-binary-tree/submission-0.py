# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def equal(root, subRoot):
            if not root and not subRoot:
                return True
            if not root and subRoot:
                return False
            if root and not subRoot:
                return False

            if root.val == subRoot.val:
                return equal(root.right, subRoot.right) and equal(root.left, subRoot.left)
            else:
                return False
        
        if not root and subRoot:
            return False
        if root and not subRoot:
            return True
        
        if equal(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
        