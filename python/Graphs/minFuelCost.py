from typing import List
from math import ceil
# 2477. Minimum Fuel Cost to Report to the Capital
# Leetcode medium

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # some variation of DFS that starts at node 0
        if not roads: 
            return 0
        adj = {}

        for i in range(len(roads)):
            v1 = roads[i][0]
            v2 = roads[i][1]
            if v1 not in adj:
                adj[v1] = [v2]
            else:
                adj[v1].append(v2)
            if v2 not in adj:
                adj[v2] = [v1]
            else:
                adj[v2].append(v1)
        litres = 0
        def dfsVisit(node, parent):
            nonlocal res
            passengers = 0
            for child in adj[node]:
                if child != parent:
                    p = dfsVisit(child, node)
                    passengers += p
                    res += int(ceil(p/seats))
            return passengers + 1
        res = 0
        dfsVisit(0, -1)
        return res

