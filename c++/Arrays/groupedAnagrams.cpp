#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagramsSoln1(vector<string> &strs)
    {
        unordered_map<string, vector<string>> mp;
        for (auto x : strs)
        {
            string word = x;
            sort(word.begin(), word.end());
            mp[word].push_back(x);
        }
        vector<vector<string>> ans;
        for (auto x : mp)
        {
            ans.push_back(x.second);
        }
        return ans;
    }
    vector<vector<string>> groupAnagramsSoln2(vector<string> &strs)
    {
        map<vector<int>, vector<string>> groups = {};
        for (int i = 0; i < strs.size(); ++i)
        {
            string curr = strs[i];
            vector<int> count(26, 0);
            for (int j = 0; j < curr.size(); ++j)
            {
                int idx = curr[j] - 'a';
                count[idx] += 1;
            }
            if (groups.find(count) == groups.end())
            {
                groups[count] = {};
            }
            groups[count].push_back(curr);
        }
        vector<vector<string>> toret = {};
        for (auto const &it : groups)
        {
            toret.push_back(it.second);
        }
        return toret;
    }
};

void printVectorString(vector<vector<string>> &res)
{
    cout << "[" << endl;
    for (int x = 0; x < res.size(); ++x)
    {
        vector<string> currVec = res[x];
        cout << "    [";
        for (int y = 0; y < currVec.size(); ++y)
        {
            string item = currVec[y];
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

int main()
{
    Solution soln = Solution();
    vector<string> ex1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> results = soln.groupAnagramsSoln1(ex1);
    printVectorString(results);
    return 0;
}
