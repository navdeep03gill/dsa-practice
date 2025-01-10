import math
import os
import random
import re
import sys
from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.taskCount = 0

    def addEdgesFromArray(self, a, b):
        for i in range(len(a)):
            fromNode = b[i]
            toNode = a[i]
            self.graph[fromNode].append(toNode)
        for key, value in self.graph.items():
            print(key, ": ", value)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self, tasks):
        stack = []
        visited = set()

        def dfsmodified(task):
            visited.add(task)
            for dependency in self.graph[task]:
                if dependency not in visited:
                    dfsmodified(dependency)
            stack.append(task)

        for task in tasks:
            if task not in visited:
                dfsmodified(task)
        
        for t in stack[::-1]:
            print(t, end=' ')
        
        return stack[::-1]

    def dfsVisit(self, v, visited):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsVisit(neighbour, visited)
            
    def dfs(self, v):
        visited = set()
        self.dfsVisit(v, visited)


    
    def findDependencyPath(self, tasks):
        sorted_tasks = self.topologicalSort(tasks)
        print(sorted_tasks)

        visited = [False] * 8
        def bfs(startNode):
            queue = deque()
            visited[startNode] = True
            queue.append(startNode)
            while queue:
                toAdd = True
                currentNode = queue.popleft()
                print(currentNode, end=' ')
                for neighbor in self.graph[currentNode]:
                    if not visited[neighbor]:
                        visited[neighbor] = True 
                        queue.append(neighbor)
                    else:
                        toAdd = False
                        visited[currentNode] = False
            return visited

        for task in sorted_tasks:
            if task not in visited:
                bfs(task)
        return visited
                 

# def make_graph(a, b):
#     graph = {}
#     for i in range(len(a)):
#         fromNode = b[i]
#         toNode = a[i]
#         if fromNode not in graph:
#             graph[fromNode] = set()
#         graph[fromNode].add(toNode)
#     for key, value in graph.items():
#         print(key, ": ", value)
#     return graph

def taskSchedule(n: int, a, b, tasks):
    g = Graph()
    g.addEdgesFromArray(a, b)
    visited = g.findDependencyPath(tasks)
    return visited


if __name__ == '__main__':
    n = 7
    a = [1, 2, 3, 4, 6, 5]
    b = [7, 6, 4, 1, 2, 1]

    allTasks = [7, 6, 4, 1, 2]

    sorted = taskSchedule(n, a, b, allTasks)
    print("Task Schedule ", sorted)


