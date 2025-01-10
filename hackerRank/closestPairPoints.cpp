#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cstdlib>

using namespace std;

class Point
{
public:
    int x, y;
};

int xCompare(const void *a, const void *b)
{
    Point *p1 = (Point *)a;
    Point *p2 = (Point *)b;
    if (p1->x > p2->x)
    {
        return 1;
    }
    else if (p1->x < p2->x)
    {
        return -1;
    }
    return 0;
}

int yCompare(const void *a, const void *b)
{
    Point *p1 = (Point *)a;
    Point *p2 = (Point *)b;
    if (p1->y > p2->y)
    {
        return 1;
    }
    else if (p1->y < p2->y)
    {
        return -1;
    }
    return 0;
}

float getDistance(Point a, Point b)
{
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

float bruteForce(Point P[], int n)
{
    float res = INT_MAX;
    vector<Point> twoPoints(2);
    for (int i = 0; i < n; ++i)
    {
        Point curr = P[i];
        for (int j = i + 1; j < n; ++j)
        {
            Point next = P[j];
            float tmp = getDistance(curr, next);
            if (tmp < res)
            {
                res = tmp;
                twoPoints[0] = curr;
                twoPoints[1] = next;
            }
        }
    }
    cout << "(" << twoPoints[0].x << ", " << twoPoints[0].y << ") (" << twoPoints[1].x << ", " << twoPoints[1].y << ")" << endl;
    return res;
}

float stripClosest(Point strip[], int n, float dist)
{
    qsort(strip, n, sizeof(Point), yCompare);
    int z = 0;
    float minDist = dist;
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n && (strip[j].y - strip[i].y) < minDist; ++j)
        {
            minDist = min(minDist, getDistance(strip[i], strip[j]));
        }
    }
    return minDist;
}

float closestUtil(Point P[], int n)
{
    if (n <= 3)
    {
        return bruteForce(P, n);
    }
    int mid = n / 2;
    Point midPoint = P[mid];

    float dl = closestUtil(P, mid);
    float dr = closestUtil(P + mid, n - mid);

    float d = min(dl, dr);
    Point strip[n];
    int j = 0;
    for (int i = 0; i < n; ++i)
    {
        if (abs(midPoint.x - P[i].x) < d)
        {
            strip[j] = P[i], j++;
        }
    }

    return min(d, stripClosest(strip, j, d));
}

float closest(Point P[], int n)
{
    qsort(P, n, sizeof(Point), xCompare);
    cout << "{" << endl;
    for (int i = 0; i < n; ++i)
    {
        Point it = P[i];

        cout << "  " << it.x << ": " << it.y << endl;
    }
    cout << "}" << endl;

    return closestUtil(P, n);
}

int main()
{
    Point P[] = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}};
    int n = sizeof(P) / sizeof(P[0]);
    float result = closest(P, n);
    cout << result << endl;

    Point P2[] = {{6, 3}, {2, 30}, {25, 1}, {5, 1}, {12, 10}, {3, 4}};
    n = sizeof(P2) / sizeof(P2[0]);
    result = closest(P2, n);
    cout << result << endl;
    return 0;
}
