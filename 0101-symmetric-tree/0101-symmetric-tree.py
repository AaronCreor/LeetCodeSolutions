# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        stack1 = [root.left]
        stack2 = [root.right]
        arr1 = []
        arr2 = []

        while stack1:
            node = stack1.pop()
            if node:
                arr1.append(node.val)
                stack1.append(node.left)
                stack1.append(node.right)
            else:
                arr1.append(None)
        while stack2:
            node = stack2.pop()
            if node:
                arr2.append(node.val)
                stack2.append(node.right)
                stack2.append(node.left)
            else:
                arr2.append(None)

        print (arr1)
        print (arr2)

        if arr1 == arr2:
            return True
        else:
            return False