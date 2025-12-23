# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            inorder(node.right)
            values.append(node.val)

        values = []

        inorder(root)

        return values
