
# 207. Course Schedule


from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {}
        for course in range(0, numCourses):
            reqs[course] = []
        for reqArr in prerequisites:
            if (reqArr[0] == reqArr[1]):
                return False
            adjArr = reqs[reqArr[0]]
            for i in adjArr:
                if reqArr[1] == i:
                    return False
            
            reqs[reqArr[1]].append(reqArr[0])

        # Detect if there's a cycle in the graph using DFS
        def dfs(adj, v, visited, recStack):
            visited[v] = True
            recStack[v] = True
            for w in adj[v]:
                if visited[w] == False:
                    if dfs(adj, w, visited, recStack) == True:
                        return True
                elif recStack[w] == True:
                    return True
            recStack[v] = False
            return False

        # initialize visited and recursion stack arrays
        visited = [0 for i in range(numCourses)]
        recStack = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if visited[i] == 0:
                res = dfs(reqs, i, visited, recStack)
                if res == True:
                    return False
        return True
        

prerequisites = [[0,1],[3,1],[1,3],[3,2]]
soln = Solution()
res = soln.canFinish(4, prerequisites)
print(res)

prerequisites = [
    [481,475],[196,63],[438,33],[212,328],[268,20],[226,288],[436,487],
    [199,494],[421,279],[369,14],[92,91],[183,174],[271,15],[4,435],
    [435,47],[217,460],[216,319],[468,125],[115,1],[435,383],[192,136],
    [86,103],[336,342],[5,301],[255,253],[185,37],[323,168],[417,241],
    [151,208],[347,53],[180,329],[198,452],[31,419],[406,74],[324,105],
    [164,494],[281,316],[139,318],[269,214],[21,269],[271,234],[142,50],
    [304,375],[285,438],[120,251],[275,423],[447,91],[420,443],[163,476],
    [436,423],[76,487],[3,443],[262,309],[398,194],[26,468],[413,241],
    [187,472],[279,58],[29,48],[173,250],[423,499],[456,242],[34,102],
    [42,376],[286,159],[147,55],[208,449],[352,86],[147,228],[111,306],
    [108,238],[297,290],[199,472],[263,451],[383,116],[441,465],[490,396],
    [39,342],[16,441],[175,405],[139,70],[377,370],[244,276],[379,188],
    [175,188],[3,165],[291,485],[162,293],[336,140],[236,61],[297,424],
    [413,403],[75,161],[148,232],[9,313],[260,186],[390,116],[282,350],
    [239,357],[33,285],[231,24],[342,82],[58,210],[423,356]]
res = soln.canFinish(500, prerequisites)
print(res)
