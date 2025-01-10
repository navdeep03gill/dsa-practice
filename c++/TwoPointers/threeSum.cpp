#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;
class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        set<vector<int>> toret;
        sort(nums.begin(), nums.end());
        this->printResult(nums);
        int i = 0;
        while (i < nums.size())
        {
            int target = -(nums[i]);
            int l = i + 1;
            int r = nums.size() - 1;
            while (l < r)
            {
                int left = nums[l];
                int right = nums[r];
                int res = target - left - right;
                if (res == 0)
                {
                    toret.insert({nums[i], nums[l], nums[r]});
                    l += 1;
                    r -= 1;
                }
                else if (res > 0)
                    l += 1;
                else
                    r -= 1;
            }
            i += 1;
        }
        vector<vector<int>> fin;
        for (auto it : toret)
        {
            fin.push_back(it);
        }
        return fin;
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
    void printVectorString(vector<vector<int>> &res)
    {

        cout << "[" << endl;
        for (int x = 0; x < res.size(); ++x)
        {
            vector<int> currVec = res[x];
            cout << "    [";
            for (int y = 0; y < currVec.size(); ++y)
            {
                int item = currVec[y];
                if (y == currVec.size() - 1)
                    cout << item;
                else
                    cout << item << ", ";
            }
            if (x == res.size() - 1)
                cout << "]" << endl;
            else
                cout << "]," << endl;
        }
        cout << "]" << endl;
    }
};

int main()
{
    cout << "Running" << endl;
    Solution soln = Solution();
    vector<int> s = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> result = soln.threeSum(s);
    cout << "\nFinal Result ex1:" << endl;
    soln.printVectorString(result);
    return 0;
}
