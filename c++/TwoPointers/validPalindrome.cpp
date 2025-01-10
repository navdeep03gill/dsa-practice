#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        vector<char> modifiedS;
        for (int i = 0; i < s.size(); ++i)
        {
            char curr = s[i];
            char fin;
            // to Lower Case
            if (curr <= 'Z' && curr >= 'A')
            {
                fin = curr + 32;
            }
            // check number or lowercase
            else if ((curr >= '0' && curr <= '9') || (curr >= 'a' && curr <= 'z'))
            {
                fin = curr;
            }
            else
            {
                continue;
            }
            modifiedS.push_back(fin);
        }
        int l = 0;
        int r = modifiedS.size() - 1;
        bool toret = 1;
        while (l < r)
        {
            if (modifiedS[l] != modifiedS[r])
            {
                toret = 0;
                break;
            }
            l += 1;
            r -= 1;
        }
        return toret;
    }
};

int main()
{
    cout << "Running" << endl;
    Solution soln = Solution();
    string s = "A man, a plan, a canal: Panama";
    bool result = soln.isPalindrome(s);
    cout << result << endl;
    return 0;
}
