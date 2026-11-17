# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque()
        current = root
        queue.append(current)
        ret = []
        if root is None:
            return []

        while queue:
            
            level = []
            for i in range(len(queue)):
                current = queue.pop()
                level.append(current.val)
                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)

            ret.append(level)
        return ret
        