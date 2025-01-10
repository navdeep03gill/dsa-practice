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
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r)
        {
            int mid = (l + r) / 2;
            if (nums[mid] == target)
            {
                return mid;
            }
            else if (nums[mid] < target)
            {
                l = mid + 1;
            }
            else
            {
                r = mid - 1;
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
    Solution *soln = new Solution();
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 9;
    int result = soln->search(nums, target);
    printVec(nums);
    cout << result << endl;
}
