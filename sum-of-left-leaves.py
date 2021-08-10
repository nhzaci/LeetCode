# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def getLeftLeaves(root, from_left):
            if not root:
                return []

            roots = []
            if not root.left and not root.right and from_left:
                return [root.val]
            if root.left:
                roots += getLeftLeaves(root.left, True)
            if root.right:
                roots += getLeftLeaves(root.right, False)
            return roots
        return sum(getLeftLeaves(root, False))
