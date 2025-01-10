#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        if (height.size() <= 1)
            return 0;
        int trapping = 0;
        int n = height.size();
        vector<int> left(n);
        left[0] = height[0];
        for (int i = 1; i < n; ++i)
        {
            left[i] = max(left[i - 1], height[i]);
        }
        vector<int> right(n);
        right[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; --i)
        {
            right[i] = max(right[i + 1], height[i]);
        }
        for (int i = 0; i < n; ++i)
        {
            trapping += min(left[i], right[i]) - height[i];
        }
        return trapping;
    }
    void printResult(vector<int> &nums)
    {
        cout << "[";
        for (int i = 0; i < nums.size(); ++i)
        {
            if (i == nums.size() - 1)
                cout << nums[i];
            else
                cout << nums[i] << ", ";
        }
        cout << "]" << endl;
    }
};

int main()
{
    cout << "Running" << endl;
    Solution soln = Solution();
    vector<int> s = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int result = soln.trap(s);
    cout << "\nFinal Result ex1:" << endl;
    cout << result << endl;
    vector<int> s2 = {4, 2, 0, 3, 2, 5};
    result = soln.trap(s2);
    cout << "\nFinal Result ex2:" << endl;
    cout << result << endl;
    return 0;
}
