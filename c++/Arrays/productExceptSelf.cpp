#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> toret(n, 1);
        vector<int> prefix(n, 1);
        vector<int> suffix(n, 1);
        for (int i = 1; i < n; ++i)
        {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        for (int i = n - 2; i >= 0; --i)
        {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }
        for (int i = 0; i < n; ++i)
        {
            toret[i] = prefix[i] * suffix[i];
        }
        return toret;
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
    Solution soln = Solution();
    vector<int> ex1 = {1, 2, 3, 4};
    vector<int> res1 = soln.productExceptSelf(ex1);
    soln.printResult(res1);
    return 200;
}
