# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque()
        queue.append([root, 0])

        ret = []

        while queue:
            node, depth = queue.popleft()
            if node:
                if len(ret) == depth:
                    ret.append([node.val])
                else:
                    ret[depth].append(node.val)

                queue.append([node.left, depth+1])
                queue.append([node.right, depth+1])

        return ret                    
                

        