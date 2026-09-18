# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        mindist = float('inf')
        minval = float('inf')
        # base conditions.
        def check(root, target):
            nonlocal mindist
            nonlocal minval
            if not root:
                return

            if abs(root.val - target) < mindist:
                mindist = abs(root.val - target)
                minval = root.val

            if root.val < target:
                check(root.right, target)
            elif root.val > target:
                check(root.left, target)
            else:
                return
        check(root, target)

        return minval

        

         
   
        