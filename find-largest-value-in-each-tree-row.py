# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        NEG_INF = -math.inf
        largest = {}
        def traverse(node, level=0):
            nonlocal largest
            if not node:
                return
            else:
                largest[level] = max(largest.get(level, NEG_INF), node.val)
                if node.right and node.left:
                    traverse(node.right, level + 1)
                    traverse(node.left, level + 1)
                elif node.right:
                    traverse(node.right, level + 1)
                elif node.left:
                    traverse(node.left, level + 1)
        traverse(root)
        return largest.values()
        
