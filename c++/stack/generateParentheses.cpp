#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cstdlib>

using namespace std;

class Solution
{
public:
    void dfs(int left, int right, int n, string s, vector<string> &parens)
    {
        if (s.size() == n * 2)
        {
            parens.push_back(s);
        }
        if (left < n)
        {
            dfs(left + 1, right, n, s + '(', parens);
        }
        if (left > right)
        {
            dfs(left, right + 1, n, s + ')', parens);
        }
    }

    vector<string> generateParenthesis(int n)
    {
        vector<string> parens;
        this->dfs(0, 0, n, "", parens);
        return parens;
    }

    void printResult(vector<string> &nums)
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
    vector<string> parentheses = soln->generateParenthesis(n);
    soln->printResult(parentheses);
    return 0;
}
