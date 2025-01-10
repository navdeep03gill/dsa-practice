#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cstdlib>
#include <utility>
#include <stack>

using namespace std;

class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        int n = temperatures.size();
        vector<int> soln(n);
        stack<pair<int, int>> st;
        for (int i = n - 1; i >= 0; --i)
        {
            while (!st.empty() && temperatures[i] >= st.top().first)
            {
                st.pop();
            }
            if (st.empty())
            {
                soln[i] = 0;
            }
            else
            {
                soln[i] = st.top().second - i;
            }
            pair<int, int> item;
            item.first = temperatures[i];
            item.second = i;
            st.push(item);
        }
        return soln;
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
    Solution *soln = new Solution();
    int n = 5;
    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};
    vector<int> tempResult = soln->dailyTemperatures(temperatures);
    soln->printResult(tempResult);
    return 0;
}
