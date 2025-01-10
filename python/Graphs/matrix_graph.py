from typing import List
from collections import deque

class UnweightedMatrixGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for column in range(vertices)] 
                            for row in range(vertices)]
    
    def set_edge(self, from_node, to_node):
        # error checking
        if from_node >= len(self.adj_matrix) or to_node >= len(self.adj_matrix):
            print("set_edge error: index out of range; from_node:", from_node, ", to_node:", to_node)
        self.adj_matrix[from_node][to_node] = 1
        #self.adj_matrix[to_node][from_node] = 1

    def print_graph(self):
        print("[")
        n = len(self.adj_matrix)
        for i in range(n):
            m = len(self.adj_matrix[i])
            print("\t[", end='')
            for j in range(m-1):
                print(f"{self.adj_matrix[i][j]}, ", end='')
            print(f"{self.adj_matrix[i][m-1]}]")
        print("]")

    def bfs(self, s):
        pred = [None for i in range(self.V)]
        dist = [float('inf') for i in range(self.V)]
        visited = [False for i in range(self.V)]
        q = deque()
        visited[s] = True
        dist[s] = 0
        q.append(s)
        while len(q) > 0:
            u = q.popleft() # pop from the left
            for v in range(self.V):    # explore all neighbours of u
                if self.adj_matrix[u][v] is None:
                    continue
                if not visited[v]:
                    pred[v] = u
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    q.append(v)
        return visited, pred, dist
    """
    def dfs_visit(self, u, visited, dist):
        visited.add(u)
        for v in range(self.V):
            if self.adj_matrix[u][v] is not None:
                if v not in visited:
                    dist[v] = dist[u] + 1
                    self.dfs_visit(v, visited, dist)

    """
    def dfs(self, s):
        visited = set()
        pred = [None for i in range(self.V)]
        discovery_time = [float("inf") for i in range(self.V)]
        finish_time = [float("inf") for i in range(self.V)]
 
        time = [0]
    
        def dfs_visit(u):
            visited.add(u)
            time[0] += 1
            discovery_time[u] = time[0]
            for v in range(self.V):
                if self.adj_matrix[u][v] is not None:
                    if v not in visited:
                        pred[v] = u
                        dfs_visit(v)
                
            time[0] += 1
            finish_time[u] = time[0]
        dfs_visit(s)
        return visited, pred, discovery_time, finish_time



def numIslands(matrix):

    # return integer representing islands
    return 0

# directed graph

def main():
    vertices = 3
    g = UnweightedMatrixGraph(vertices)
    edges = [(0,1), (1,0), (1,2), (2,1), (2,0), (0,2)]
    for edge in edges:
        g.set_edge(edge[0], edge[1])
    g.print_graph()
    visited, pred, dist = g.bfs(0)

    print("DFS")
    visited, pred, discovery_time, finish_time = g.dfs(0)
    print("Visited Set:", visited)
    print("Predecessor Array:", pred)
    print("Discovery Array:", discovery_time)
    print("Finish Array:", finish_time)
    return 0

#Driver
if __name__ == "__main__":
    # create the graph given in above figure
    main()

