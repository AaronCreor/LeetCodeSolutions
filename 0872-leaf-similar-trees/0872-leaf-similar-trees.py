# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        curr1 = [root1]
        curr2 = [root2]
        list1 = []
        list2 = []
        while curr1:
            node = curr1.pop()
            if node:
                if node.left is None and node.right is None:
                    list1.append(node.val)
                else:
                    curr1.append(node.left)
                    curr1.append(node.right)
        while curr2:
            node = curr2.pop()
            if node:
                if node.left is None and node.right is None:
                    list2.append(node.val)
                else:
                    curr2.append(node.left)
                    curr2.append(node.right)
        if list1 == list2:
            return True
        else:
            return False
        