#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int currMax = 0;
        int l = 0;
        int r = height.size() - 1;
        while (l < r)
        {
            int area = min(height[l], height[r]) * (r - l);
            if (area > currMax)
                currMax = area;
            if (height[r] < height[l])
                r -= 1;
            else
                l += 1;
        }
        return currMax;
    }
};

int main()
{
    cout << "Running" << endl;
    Solution soln = Solution();
    vector<int> s = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int result = soln.maxArea(s);
    cout << "\nFinal Result ex1:" << endl;
    cout << result << endl;
    return 0;
}
