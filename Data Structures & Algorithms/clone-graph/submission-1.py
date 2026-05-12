"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldtonew = {}

        def dfs(node):
            if node in oldtonew: #if copy already present return it
                return oldtonew[node]
            # else create a copy
            copy = Node(node.val)
            oldtonew[node] = copy # add to hashset
            for n in node.neighbors: # add each neighbor
                copy.neighbors.append(dfs(n)) 

            return copy

        return dfs(node) if node else None
