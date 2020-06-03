# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, root, mir):
        if not root:
            mir = None
            return None
        mir = TreeNode(root.val)
        mir.right = self.invert(root.left, mir.right)
        mir.left = self.invert(root.right, mir.left)
        return mir
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.invert(root, None)
            
