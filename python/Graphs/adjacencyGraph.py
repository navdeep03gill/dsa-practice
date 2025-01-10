from typing import List
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for i in range(self.V)]

    def add_edge(self, u, v):
        self.adj[u] = v
        self.adj[v] = u

    def set_edges(self, edges):
        self.adj = edges
    
    def dfs(self, s):
        visited = set()
        pred = [None for i in range(self.V)]
        # discovery_time = [float("inf") for i in range(self.V)]
        # finish_time = [float("inf") for i in range(self.V)]
        def dfs_visit(u):
            visited.add(u)
            for v in self.adj[u]:
                if v not in visited:
                    pred[v] = u
                    dfs_visit(v)
        dfs_visit(s)
        return visited   
            

def peak_matrix(matrix, x, y):
    if x < 0 or y < 0 or x+1 > len(matrix) or y+1 > len(matrix):
        return False
    if matrix[x][y] == 1:
        return True
    return False

def check_surrounding(matrix, x, y, ):
    if x == 0:
        if y == 0:
            n1 = peak_matrix(matrix, x+1, y)
            n1 = peak_matrix(matrix, x+1, y)

def edge_helper(vertices, edge_graph, vertex, x, y):
    n_to_node = vertices.get((x,y), None)
    if n_to_node is not None:
        edge_graph[vertex].append(n_to_node)

def create_edges(matrix, vertices, edge_graph):
    # traverse vertices. From there, check all surroundings to get edges of that vertex
    for key, value in vertices.items():
        x = key[0]
        y = key[1]
        vertex = value
        n1 = peak_matrix(matrix, x-1, y-1) #False # x-1, y-1
        n2 = peak_matrix(matrix, x-1, y) # x-1, y
        n3 = peak_matrix(matrix, x-1, y+1) # x-1, y+1
        n4 = peak_matrix(matrix, x, y-1) # x, y-1
        n5 = peak_matrix(matrix, x, y+1) # x, y+1
        n6 = peak_matrix(matrix, x+1, y-1) # x+1, y-1
        n7 = peak_matrix(matrix, x+1, y) # x+1, y
        n8 = peak_matrix(matrix, x+1, y+1) # x+1, y+1

        if n1 == True:
            edge_helper(vertices, edge_graph, vertex, x-1, y-1)
        if n2 == True:
            edge_helper(vertices, edge_graph, vertex, x-1, y)
        if n3 == True:
            edge_helper(vertices, edge_graph, vertex, x-1, y+1)
        if n4 == True:
            edge_helper(vertices, edge_graph, vertex, x, y-1)
        if n5 == True:
            edge_helper(vertices, edge_graph, vertex, x, y+1)
        if n6 == True:
            edge_helper(vertices, edge_graph, vertex, x+1, y-1)
        if n7 == True:
            edge_helper(vertices, edge_graph, vertex, x+1, y)
        if n8 == True:
            edge_helper(vertices, edge_graph, vertex, x+1, y+1)
    return


def label_vertices(matrix):
    vertices = {}
    v_number = 0
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 1:
                vertices[(i,j)] = v_number
                v_number += 1
    return vertices, v_number


def printAdjList(adj):
    print("List:")
    print("[")
    for a in range(len(adj)):
        print("   [", end="")
        curr_row = adj[a]
        for b in range(len(curr_row)):
            if b == len(curr_row) - 1:
                print(f"{curr_row[b]}", end="")
            else: 
                print(f"{curr_row[b]}, ", end="")
        print("],")
    print("]")

def num_islands(matrix):
    vertices, v_number = label_vertices(matrix)
    """
    for key, value in vertices.items():
        print(key, " ", end='')
        print(value)
    """
    edge_graph = [[] for i in range(v_number)]
    create_edges(matrix, vertices, edge_graph)
    #printAdjList(edge_graph)

    g = Graph(v_number)
    g.set_edges(edge_graph)

    islands = 0
    node_set = []
    for i in range(v_number):
        node_set.append(i)
    
    while len(node_set) > 0:
        start_node = node_set[0]
        visited = g.dfs(start_node)

        for v in visited:
            node_set.remove(v)
        islands += 1
    return islands

def main():
    mat = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
    ]
    islands = num_islands(mat)
    print("Number of islands:", islands)
    mat2 = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
    ]
    islands = num_islands(mat2)
    print("Number of islands:", islands)
    return 0

#Driver
if __name__ == "__main__":
# create the graph given in above figure

    main()


