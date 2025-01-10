#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <string>
#include <map>
#include <stack>

using namespace std;

class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> nums;
        int result = 0;
        for (int i = 0; i < tokens.size(); ++i)
        {
            if (tokens[i] == "+" || tokens[i] == "*" || tokens[i] == "/" || tokens[i] == "-")
            {
                int right = nums.top();
                nums.pop();
                int left = nums.top();
                nums.pop();
                if (tokens[i] == "+")
                    nums.push(left + right);
                else if (tokens[i] == "*")
                    nums.push(left * right);
                else if (tokens[i] == "/")
                    nums.push(left / right);
                else if (tokens[i] == "-")
                    nums.push(left - right);
            }
            else
            {
                nums.push(stoi(tokens[i]));
            }
        }
        return nums.top();
    }
};

int main()
{
    vector<string> toEval = {"2", "1", "+", "3", "*"};
    Solution *soln = new Solution();
    int res = soln->evalRPN(toEval);
    cout << res << endl;
}
