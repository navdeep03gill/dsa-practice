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
    int search(vector<int> &nums, int target)
    {
        if (nums.size() == 1)
        {
            if (nums[0] == target)
                return 0;
            return -1;
        }
        if (nums.size() == 2)
        {
            if (nums[0] == target)
                return 0;
            if (nums[1] == target)
                return 1;
            return -1;
        }
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r)
        {
            int m = (l + r) / 2;
            int mid = nums[m];
            // cout << l << ", " << m << ", " << r << endl;
            if (target == mid)
            {
                return m;
            }
            else if (target < mid)
            {
                if (mid <= nums[r])
                {
                    r = m - 1;
                }
                else
                {
                    if (target <= nums[r])
                    {
                        l = m + 1;
                    }
                    else
                    {
                        r = m - 1;
                    }
                }
            }
            else
            {
                if (nums[l] <= mid)
                {
                    l = m + 1;
                }
                else
                {
                    if (target >= nums[l])
                    {
                        r = m - 1;
                    }
                    else
                    {
                        l = m + 1;
                    }
                }
            }
        }
        return -1;
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
    vector<int> nums = {5, 1, 2, 3, 4};
    int minResult = soln.search(nums, 4);
    printVec(nums);
    cout << minResult << endl;
}
