#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cstdlib>
#include <utility>
#include <stack>
#include <map>

using namespace std;

class Solution
{
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        map<int, int> posToSpeed;
        int n = position.size();
        vector<vector<int>> sortedCars;
        vector<float> time;
        for (int i = 0; i < n; ++i)
        {
            posToSpeed[position[i]] = speed[i];
        }
        for (map<int, int>::iterator i = posToSpeed.begin(); i != posToSpeed.end(); i++)
        {
            vector<int> toAdd = {i->first, i->second};
            sortedCars.push_back(toAdd);
            float timeItem = float(target - i->first) / float(i->second);
            time.push_back(timeItem);
        }
        stack<float> fleet;
        int results = 0;
        for (int i = n - 1; i >= 0; --i)
        {
            while (!fleet.empty() && fleet.top() < time[i])
            {
                fleet.pop();
            }
            if (fleet.empty())
            {
                results += 1;
            }
            fleet.push(time[i]);
        }
        return results;
    }
};

int main()
{
    Solution *soln = new Solution();
    int target = 12;
    vector<int> position = {10, 8, 0, 5, 3};
    vector<int> speed = {2, 4, 1, 1, 3};
    int fleets = soln->carFleet(target, position, speed);
    cout << fleets << endl;
    return 0;
}
