import sys
import math

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def printPoint(self):
        print("(", self.x, ", ", self.y, ")")


def getX(p):
    return p.x

def getY(p):
    return p.y

def distance(p, q):
    return math.sqrt((p.x - q.x)*(p.x - q.x) + (p.y - q.y)*(p.y - q.y))

def bruteForce(P, n):
    res = float("inf")
    twoPoints = [None] * 2
    for i in range(0, n):
        for j in range(i+1, n):
            #res = min(res, distance(P[i], P[j]))
            if res > distance(P[i], P[j]):
                res = distance(P[i], P[j])
                twoPoints[0] = P[i]
                twoPoints[1] = P[j]
                
    if twoPoints[0]:
        twoPoints[0].printPoint()
        twoPoints[1].printPoint()
        print(res)
    return res

def stripClosest(strip, n, dist):
    minDist = dist
    # find shortest distance between two points in strip
    for i in range(n):
        for j in range(i+1, n):
            if (strip[i].y - strip[j].y) < minDist:
                minDist = min(minDist, distance(strip[i], strip[j]))
    return minDist


def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)

    mid = n // 2
    midPoint = P[mid]

    dl = closestUtil(P, mid)
    dr = closestUtil(P[mid:], n - mid)

    d = min(dl, dr)

    strip = []
    j = 0
    for i in range(n):
        if (midPoint.x - P[i].x) < d:
            strip.append(P[i])
            j += 1
    
    strip.sort(key=getY)
    return min(d, stripClosest(strip, j, d))

def closest(P, n):
    P.sort(key=getX)
    print("{")
    for p in P:
        print("   ", end="")
        p.printPoint()
    print("}")
    return closestUtil(P, n)


if __name__ == "__main__":
    P = [Point(x=2, y=3), Point(x=12, y=30),
         Point(x=40, y=50), Point(x=5, y=1), Point(x=12, y=10), Point(x=3, y=4)]
    n = len(P)

    print("The smallest distance is", closest(P, n))

