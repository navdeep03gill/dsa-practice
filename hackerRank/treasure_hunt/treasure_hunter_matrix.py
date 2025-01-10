from re import L
import sys

INF = 99999

class GraphMatrix():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                        for row in range(vertices)]
           
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
    # utility function to find vertex with min distance value
    # from the set of vertices not yet included in the shortest path tree
    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = 0
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            # Pick minimum distance vertex to the src,
            # from the set of vertices not yet processed - 
            # i.e. not in sptSet
            x = self.minDistance(dist, sptSet)

            sptSet[x] = True

            # Update distance values for the adjacent vertices
            # of the picked verted only if the current distance
            # is greater than the new distance and the vertex is 
            # not in the shortest path tree
            for y in range(self.V):
                # if valid vertex and not visited and dist should be updated
                if self.graph[x][y] < INF and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)



def peekGameBoard(game_board, x, y):
    if game_board[x][y] == 'X':
        return INF
    elif game_board[x][y] == '':
        return 0
    elif game_board[x][y] == 'T':
        return 0
    return int(game_board[x][y])

def checkSurroundings(adj, numbered_adj, game_board, x, y):
    if peekGameBoard(game_board, x, y) == INF:
        return adj
    curr_idx = numbered_adj[x][y]
    piece1 = None
    piece2 = None
    piece3 = None
    piece4 = None
    idx_1 = None
    idx_2 = None
    idx_3 = None
    idx_4 = None
    if x == 0:
        if y == 0:
            piece1 = peekGameBoard(game_board, x+1, y)
            piece2 = peekGameBoard(game_board, x, y+1)
            idx_1 = numbered_adj[x+1][y]
            idx_2 = numbered_adj[x][y+1]
        elif y == len(numbered_adj[0]) - 1:
            piece1 = peekGameBoard(game_board, x+1, y)
            piece2 = peekGameBoard(game_board, x, y-1)
            idx_1 = numbered_adj[x+1][y]
            idx_2 = numbered_adj[x][y-1]
        else:
            piece1 = peekGameBoard(game_board, x+1, y)
            piece2 = peekGameBoard(game_board, x, y+1)
            piece3 = peekGameBoard(game_board, x, y-1)
            idx_1 = numbered_adj[x+1][y]
            idx_2 = numbered_adj[x][y+1]
            idx_3 = numbered_adj[x][y-1]

    elif x == len(numbered_adj) - 1:
        if y == 0:
            piece1 = peekGameBoard(game_board, x-1, y)
            piece2 = peekGameBoard(game_board, x, y+1)
            idx_1 = numbered_adj[x-1][y]
            idx_2 = numbered_adj[x][y+1]
        elif y == len(numbered_adj[0]) - 1:
            piece1 = peekGameBoard(game_board, x-1, y)
            piece2 = peekGameBoard(game_board, x, y-1)
            idx_1 = numbered_adj[x-1][y]
            idx_2 = numbered_adj[x][y-1]
        else:
            piece1 = peekGameBoard(game_board, x-1, y)
            piece2 = peekGameBoard(game_board, x, y-1)
            piece3 = peekGameBoard(game_board, x, y+1)
            idx_1 = numbered_adj[x-1][y]
            idx_2 = numbered_adj[x][y-1]
            idx_3 = numbered_adj[x][y+1]
    
    else:
        if y == 0:
            piece1 = peekGameBoard(game_board, x-1, y)
            piece2 = peekGameBoard(game_board, x+1, y)
            piece3 = peekGameBoard(game_board, x, y+1)
            idx_1 = numbered_adj[x-1][y]
            idx_2 = numbered_adj[x+1][y]
            idx_3 = numbered_adj[x][y+1]
        elif y == len(numbered_adj[0]) - 1:
            piece1 = peekGameBoard(game_board, x-1, y)
            piece2 = peekGameBoard(game_board, x+1, y)
            piece3 = peekGameBoard(game_board, x, y-1)
            idx_1 = numbered_adj[x-1][y]
            idx_2 = numbered_adj[x+1][y]
            idx_3 = numbered_adj[x][y-1]
        else:
            piece1 = peekGameBoard(game_board, x-1, y)
            piece2 = peekGameBoard(game_board, x+1, y)
            piece3 = peekGameBoard(game_board, x, y+1)
            piece4 = peekGameBoard(game_board, x, y-1)
            idx_1 = numbered_adj[x-1][y]
            idx_2 = numbered_adj[x+1][y]
            idx_3 = numbered_adj[x][y+1]
            idx_4 = numbered_adj[x][y-1]
        
    if piece1 is not None and idx_1 is not None:
        adj[curr_idx][idx_1] = piece1
    if piece2 is not None and idx_2 is not None:
        adj[curr_idx][idx_2] = piece2
    if piece3 is not None and idx_3 is not None:
        adj[curr_idx][idx_3] = piece3
    if piece4 is not None and idx_4 is not None: 
        adj[curr_idx][idx_4] = piece4
    if curr_idx == 4:
        print(idx_1, idx_2, idx_3, idx_4)
        print(piece1, piece2, piece3, piece4)

    #adj[curr_idx][curr_idx] = 0

    return adj


def makeAdjMatrix(game_board):
    n = len(game_board)
    m = len(game_board[0])
    ith_item = 0

    numbered_adj = []
    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(ith_item)
            ith_item += 1
        numbered_adj.append(new_row)

    adj = [[INF for i in range(ith_item)]
            for j in range(ith_item)]

    for i in range(n):
        for j in range(m):
            # we have an i and f value
            adj = checkSurroundings(adj, numbered_adj, game_board, i, j)
        
    printMatrix(adj)
    return adj

  

def hunt_treasure(game_board, health, pos):
    return 0


def printMatrix(matrix):
    print("Matrix:")
    print("[")
    for i in range(len(matrix)):
        print("    [", end="")
        curr_row = matrix[i]
        for j in range(len(curr_row) - 1):
            print(curr_row[j], ", ", end="")
        print(curr_row[len(curr_row) - 1], "]")
    print("]") 

GameBoard1 = [
    ['','5','X'],
    ['','2',''],
    ['','1','T'],
]

adjacencyMatrix1 = [
    [INF, 5, INF, 0, INF, INF, INF, INF, INF],
    [0, INF, INF, INF, 2, INF, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF],
    [0, INF, INF, INF, 2, INF, 0, INF, INF],
    [INF, 5, INF, 0, INF, 0, INF, 1, INF],
    [INF, INF, INF, INF, 2, INF, INF, INF, 0],
    [INF, INF, INF, 0, INF, INF, INF, 1, INF],
    [INF, INF, INF, INF, 2, INF, 0, INF, 0],
    [INF, INF, INF, INF, INF, 0, INF, 1, INF],
]


GameBoard2 = [
    ['','5','X'],
    ['','2',''],
    ['','1','T'],
]

def compare_manual_and_auto(auto_adj, manual_adj):
    if len(auto_adj) != len(manual_adj):
        print("different n")
    if len(auto_adj[0]) != len(manual_adj[0]):
        print("different m")
    for i in range(len(auto_adj)):
        for j in range(len(auto_adj[0])):
            if auto_adj[i][j] != manual_adj[i][j]:
                print(i, j, auto_adj[i][j], manual_adj[i][j])
    return 1


if __name__ == "__main__":
    g = GraphMatrix(9)
    adj = makeAdjMatrix(GameBoard1)
    g.graph = adj
    g.dijkstra(0)
    compare_manual_and_auto(adj, adjacencyMatrix1)

