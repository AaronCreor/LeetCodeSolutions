# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        queue = deque([[root, 1]])
        while queue:
            node, depth = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return depth
                queue.append([node.left, depth+1])
                queue.append([node.right, depth+1])




        #while stack:
        #    node, depth = stack.pop()
        #    if node:
        #        stack.append([node.left, depth+1])
        #        stack.append([node.right, depth+1])
        #        if not node.left and not node.right:
        #            minDepth = min(minDepth, depth)
        #return minDepth