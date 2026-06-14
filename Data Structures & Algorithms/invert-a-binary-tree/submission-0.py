# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        self.switch_tree(root)
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    def switch_tree(self, node: Optional[TreeNode]):
        temp = node.left
        node.left = node.right
        node.right = temp