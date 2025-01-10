#include <iostream>
#include <cstdlib>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <map>

using namespace std;

typedef variant<
    std::string,
    int>
    StringOrInt;

class TimeMap
{
public:
    map<string, vector<pair<int, string>>> obj;
    TimeMap()
    {
    }

    void set(string key, string value, int timestamp)
    {
        obj[key].push_back({timestamp, value});
    }

    string get(string key, int timestamp)
    {
        int l = 0;
        int r = obj[key].size() - 1;
        string res = "";
        while (l <= r)
        {
            int m = (l + r) / 2;
            int midStamp = obj[key][m].first;
            if (midStamp <= timestamp)
            {
                l = m + 1;
                res = obj[key][m].second;
            }
            else
            {
                r = m - 1;
            }
        };
        return res;
    }
};

template <typename Type>
void printVec(vector<Type> &vec)
{
    cout << "[";
    for (int i = 0; i < vec.size(); ++i)
    {
        if (i == vec.size() - 1)
            cout << vec[i];
        else
            cout << vec[i] << ", ";
    }
    cout << "]" << endl;
}

int main()
{
    TimeMap *soln = new TimeMap();
    vector<string> functionCalls = {"TimeMap", "set", "get", "get", "set", "get", "get"};
    vector<vector<StringOrInt>> functionArgs = {
        {"void"},
        {"foo", "bar", 1},
        {"foo", 1},
        {"foo", 3},
        {"foo", "bar2", 4},
        {"foo", 4},
        {"foo", 5}};
    int nCalls = functionCalls.size();

    vector<string> toPrint;
    for (int i = 0; i < nCalls; ++i)
    {
        string fCall = functionCalls[i];
        vector<StringOrInt> argList = functionArgs[i];
        if (fCall == "TimeMap")
        {
            toPrint.push_back("null");
            continue;
        }
        else if (fCall == "set")
        {
            string key = get<std::string>(argList[0]);
            string value = get<std::string>(argList[1]);
            int timestamp = get<int>(argList[2]);
            soln->set(key, value, timestamp);
            toPrint.push_back("null");
        }
        else if (fCall == "get")
        {
            string key = get<std::string>(argList[0]);
            int timestamp = get<int>(argList[1]);
            string value = soln->get(key, timestamp);
            toPrint.push_back(value);
        }
    }
    printVec(toPrint);
    return 0;
}
