# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return None
        current = root
        stack = [current]
        while stack:
            node = stack.pop()
            if node:
                if node.val == val:
                    return node
                elif node.val < val:
                    stack.append(node.right)
                elif node.val > val:
                    stack.append(node.left)
                else:
                    return None
            else:
                return None
        return None


            