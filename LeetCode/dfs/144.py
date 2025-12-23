# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return

            values.append(node.val)
            inorder(node.left)
            inorder(node.right)

        values = []

        inorder(root)

        return values
