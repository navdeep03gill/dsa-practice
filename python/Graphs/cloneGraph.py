
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # add node 1 to queue
        if not node: return node
        q = [node]
        clones = {node.val: Node(node.val, [])}
        while q:
            cur = q.pop(0)
            cur_clone = clones[cur.val]
            for neighbor in cur.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                cur_clone.neighbors.append(clones[neighbor.val])
        return clones[node.val]

def createGraph(input):
    if not input: return input
    clone = {}
    for i in range(1, len(input) + 1):
        clone[i] = Node(i, [])
    for i in range(len(input)):
        curNode = clone[i+1]
        for j in input[i]:
            curNode.neighbors.append(clone[j])
    toprint = []
    for i in clone:
        toprint.append(i)
    print(toprint)
    return clone[1]

def printGraph(node):
    visited = {node.val: []}
    q = [node]
    while q:
        cur = q.pop(0)
        nbrs = cur.neighbors
        for nbr in nbrs:
            if (nbr.val not in visited):
                q.append(nbr)
                visited[nbr.val] = []
            visited[cur.val].append(nbr.val)
    for k,v in visited.items():
        print(k,":", v)
    return       


input1 = [[2,4],[1,3],[2,4],[1,3]]
startNode = createGraph(input1)
printGraph(startNode)
soln = Solution()
cloneGraph = soln.cloneGraph(startNode)
printGraph(cloneGraph)



        