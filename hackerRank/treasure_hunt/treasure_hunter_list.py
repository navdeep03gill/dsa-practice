from re import L
import sys
import heapq
from collections import deque

INF = sys.maxsize

class GraphAdjList:
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))

    def setAdjList(self, adjList):
        self.adj = adjList
    
    def shortestPathBFS(self, src: int, target):
        startSteps = 0
        initial_health = 5
        queue = deque([(src, startSteps, initial_health)])

        visited = {src: (0, initial_health)}
        while queue:
            current_node, steps, curr_health = queue.popleft()
            if current_node == target:
                return (steps, curr_health)
            
            for neighbor, weight in self.adj[current_node]:
                new_health = curr_health - weight
                if new_health >= 0:
                    if neighbor not in visited:
                        visited[neighbor] = (steps + 1, new_health)
                        queue.append((neighbor, steps + 1, new_health))
                    else:
                        # If the path has fewer steps or more health with the same steps, update it
                        old_steps, old_health = visited[neighbor]
                        if steps+1 < old_steps or (new_health > old_health and steps+1 <= old_steps):
                            visited[neighbor] = (steps+1, new_health)
                            queue.append((neighbor, steps + 1, new_health))
        return None

    def shortestPathDijkstra(self, src: int, treasure_node):
        # Create a priority queue to store vertices that
        # are being preprocessed

        # We are storing node, steps, damage,  
        pq = []

        startSteps = 0
        startDamage = 0
        heapq.heappush(pq, (src, startSteps, startDamage))

        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        steps = [float('inf')] * self.V
        steps[src] = 0

        damage = [float('inf')] * self.V
        damage[src] = 0

        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            u, step, d = heapq.heappop(pq)

            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If shorter steps, or same steps but lower damage
                if (damage[u] + weight) < 5:
                    if (steps[v] > steps[u] + 1) or (steps[v] == steps[u]+1 and damage[v] > damage[u] + weight):
                        steps[v] = steps[u] + 1
                        damage[v] = damage[u] + weight
                        heapq.heappush(pq, (v, steps[v], damage[v]))
        print("Node \t\t steps \t\t health")
        for i in range(self.V):
            print(f"{i} \t\t {steps[i]} \t\t {5 - damage[i]}")
        
        tSteps = steps[treasure_node] if steps[treasure_node] != float('inf') else -1
        tHealth = 5 - damage[treasure_node] if damage[treasure_node] != float('inf') else 5
        return (tSteps, tHealth)
        

def peekGameBoard(game_board, x, y):
    if game_board[x][y] == 'X':
        return None
    elif game_board[x][y] == '':
        return 0
    elif game_board[x][y] == 'T':
        return 0
    return int(game_board[x][y])

def checkSurroundings(adj, numbered_adj, game_board, x, y):
    if game_board[x][y] == 'X':
        return
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
        adj[curr_idx].append((idx_1, piece1))
    if piece2 is not None and idx_2 is not None:
        adj[curr_idx].append((idx_2, piece2))
    if piece3 is not None and idx_3 is not None:
        adj[curr_idx].append((idx_3, piece3))
    if piece4 is not None and idx_4 is not None:
        adj[curr_idx].append((idx_4, piece4))
    return

def makeAdjMatrix(game_board):
    n = len(game_board)
    m = len(game_board[0])
    ith_item = 0

    ith_item = 0

    numbered_adj = []
    for i in range(n):
        new_row = []
        for j in range(m):
            new_row.append(ith_item)
            ith_item += 1
        numbered_adj.append(new_row)

    adj = [[]
            for j in range(ith_item)]
    for i in range(n):
        for j in range(m):
            # we have an i and j value
            checkSurroundings(adj, numbered_adj, game_board, i, j)
    return adj

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

def getNumberedMatrix(game_board):
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
    return numbered_adj

def findTreasure(game_board):
    numbered_matrix = getNumberedMatrix(game_board=game_board)
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 'T':
                return numbered_matrix[i][j]
    return -1


def compare_manual_and_auto(auto_adj, manual_adj):
    if len(auto_adj) != len(manual_adj):
        print("different n")
    for i in range(len(auto_adj)):
        curr_row = auto_adj[i]
        for j in range(len(curr_row)):
            if auto_adj[i][j] != manual_adj[i][j]:
                print(i, j, auto_adj[i][j], manual_adj[i][j])
    return 1

GameBoard1 = [
    ['','5','X'],
    ['','2',''],
    ['','1','T'],
]

GameBoard2 = [
    ['','X'],
    ['2','T'],
]

GameBoard3 = [
    ['', '', '', '', ''],
    ['', 'X', 'X', 'X', ''],
    ['', 'X', '', '', ''],
    ['', 'X', '3', 'X', 'X'],
    ['', '4', '', '1', 'T'],
]

def main():
    V = 9
    adj = makeAdjMatrix(GameBoard1)
    treasure_node = findTreasure(GameBoard1)
    print("Treasure located at:", treasure_node)
    if treasure_node == -1:
        print("Treasure not found")
        return 0
    g = GraphAdjList(V)
    g.setAdjList(adj)
    result = g.shortestPathDijkstra(0, treasure_node)
    print(str(result[0]), str(result[1]))
    # struct = g.shortestPathBFS(0, treasure_node)
    # print("GameBoard1 Result:", struct)

    adj = makeAdjMatrix(GameBoard2)
    treasure_node = findTreasure(GameBoard2)
    if treasure_node == -1:
        print("Treasure not found")
        return 0
    print("Treasure located at:", treasure_node)
    Vsize = len(GameBoard2) * len(GameBoard2[0])
    g2 = GraphAdjList(Vsize)
    g2.setAdjList(adj)
    result = g2.shortestPathDijkstra(0, treasure_node)
    print(str(result[0]), str(result[1]))

    adj = makeAdjMatrix(GameBoard3)
    treasure_node = findTreasure(GameBoard3)
    if treasure_node == -1:
        print("Treasure not found")
        return 0
    print("Treasure located at:", treasure_node)
    Vsize = len(GameBoard3) * len(GameBoard3[0])
    g3 = GraphAdjList(Vsize)
    g3.setAdjList(adj)
    result = g3.shortestPathDijkstra(0, treasure_node)
    print(str(result[0]), str(result[1]))
  
    return 0


#Driver
if __name__ == "__main__":
    # create the graph given in above figure
    main()




