#include <iostream>
#include <vector>
#include <string>

using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r)
        {
            int left = numbers[l];
            int right = numbers[r];
            int res = target - left - right;
            if (res == 0)
            {
                return {l + 1, r + 1};
            }
            else if (res > 0)
            {
                l += 1;
            }
            else
            {
                r -= 1;
            }
        }
        return {-1, -1};
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
    vector<int> s = {2, 7, 11, 15};
    vector<int> result = soln.twoSum(s, 18);
    soln.printResult(result);
    return 0;
}
