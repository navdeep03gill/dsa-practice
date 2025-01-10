#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>

using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        if (s.size() % 2 == 1)
        {
            return false;
        }
        stack<char> front;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == ']' || s[i] == ')' || s[i] == '}')
            {
                if (front.empty())
                    return false;
                char f = front.top();
                front.pop();
                if (s[i] == ')' && f != '(')
                {
                    return false;
                }
                else if (s[i] == '}' && f != '{')
                {
                    return false;
                }
                else if (s[i] == ']' && f != '[')
                {
                    return false;
                }
            }
            else
            {
                front.push(s[i]);
            }
        }
        if (!front.empty())
            return false;
        return true;
    }
};

int main()
{
    cout << "Running" << endl;
    Solution soln = Solution();
    string s = "()[]{}";
    bool result = soln.isValid(s);
    cout << "\nFinal Result ex1:" << endl;
    cout << result << endl;
    string s2 = "((";
    result = soln.isValid(s2);
    cout << "\nFinal Result ex2:" << endl;
    cout << result << endl;
    return 0;
}
