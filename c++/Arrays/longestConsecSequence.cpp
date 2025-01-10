#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        set<int> elms;
        for (auto x : nums)
        {
            elms.insert(x);
        }
        int maxSeq = 0;
        for (auto i : elms)
        {
            if (elms.contains(i - 1))
            {
                continue;
            }
            vector<int> currSeq = {i};
            int rightSeq = i + 1;
            while (elms.contains(rightSeq))
            {
                currSeq.push_back(rightSeq);
                rightSeq += 1;
            }
            if (currSeq.size() > maxSeq)
            {
                maxSeq = currSeq.size();
            }
        }
        return maxSeq;
    }
};