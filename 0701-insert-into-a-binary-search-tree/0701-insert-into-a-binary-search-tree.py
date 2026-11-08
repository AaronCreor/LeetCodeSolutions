# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        x = TreeNode(val)
        y = root
        if y is None:
            root = x
        else:
            while True:
                if y.val < x.val:
                    if y.right is None:
                        y.right = x
                        break
                    y = y.right
                else:
                    if y.left is None:
                        y.left = x
                        break
                    y = y.left
        return root