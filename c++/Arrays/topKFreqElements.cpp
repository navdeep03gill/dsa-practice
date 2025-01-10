#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        map<int, int> numsHash;
        vector<int> toret;
        for (auto &it : nums)
        {
            numsHash[it]++;
        }
        vector<pair<int, int>> toSort;

        for (auto it : numsHash)
        {
            toSort.push_back(make_pair(it.second, it.first));
        }
        sort(toSort.begin(), toSort.end());
        int arrLen = toSort.size() - 1;
        for (int i = arrLen; i > arrLen - k; --i)
        {
            toret.push_back(toSort[i].second);
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
    vector<int> inp1 = {2, 5, 5, 5, 5, 5, 5, 1, 1, 1, 4, 4, 4, 4, 2, 2, 3};
    Solution soln = Solution();
    vector<int> res1 = soln.topKFrequent(inp1, 4);
    soln.printResult(res1);
    return 0;
}
