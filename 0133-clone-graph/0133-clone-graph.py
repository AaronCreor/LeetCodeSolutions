"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:#Empty case
            return None
        visited = set()
        stack = [node]
        clones = {}
        while stack:#dfs populates dictionary of old/new node relationship
            local=stack.pop()
            if local in visited:
                continue
            visited.add(local)
            clones[local] = Node(local.val)
            for neighbor in local.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

        print(clones)
        for original, clone in clones.items():
            for neighbor in original.neighbors:
                clone.neighbors.append(clones[neighbor])
        return(clones[node])
        
