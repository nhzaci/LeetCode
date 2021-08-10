# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getSeq(root):
            if not root:
                return []

            roots = []
            if not root.left and not root.right:
                return [root.val]
            if root.left:
                roots.extend(getSeq(root.left))
            if root.right:
                roots.extend(getSeq(root.right))
            return roots
        return getSeq(root1) == getSeq(root2)
