#include <iostream>
#include <cstdlib>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <map>

using namespace std;

class Solution
{
public:
    int findMin(vector<int> &nums)
    {
        if (nums.size() == 1)
            return nums[0];
        if (nums.size() == 2)
            return min(nums[0], nums[1]);
        int l = 0;
        int r = nums.size() - 1;
        int minimum = nums[0];
        while (l <= r)
        {
            int m = (l + r) / 2;
            int mid = nums[m];
            if (minimum < mid)
            {
                l = m + 1;
            }
            else
            {
                r = m - 1;
                minimum = mid;
            }
        }
        return minimum;
    }
};

template <typename Type>
void printVec(vector<Type> &vec)
{
    cout << "[";
    for (int i = 0; i < vec.size(); ++i)
    {
        if (i == vec.size() - 1)
            cout << vec[i];
        else
            cout << vec[i] << ", ";
    }
    cout << "]" << endl;
}

int main()
{
    Solution soln = Solution();
    vector<int> nums = {3, 4, 5, 1, 2};
    int minResult = soln.findMin(nums);
    printVec(nums);
    cout << minResult << endl;
}
