# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        ret1 = []
        ret2 = []
        stack1 = [p]
        stack2 = [q]

        while stack1:
            node = stack1.pop()
            if node:
                ret1.append(node.val)
                stack1.append(node.left)
                stack1.append(node.right)
            else:
                ret1.append("null")

        while stack2:
            node = stack2.pop()
            if node:
                ret2.append(node.val)
                stack2.append(node.left)
                stack2.append(node.right)
            else:
                ret2.append("null")
                
        if ret1 == ret2:
            return True
        else:
            return False