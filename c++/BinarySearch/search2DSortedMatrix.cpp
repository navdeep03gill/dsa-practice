#include <iostream>
#include <cstdlib>
#include <utility>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <map>

using namespace std;

class Solution
{
public:
    bool binarySearch(vector<int> &vec, int &target)
    {
        int l = 0;
        int r = vec.size() - 1;
        while (l <= r)
        {
            int mid = (l + r) / 2;
            if (target == vec[mid])
                return true;
            else if (target < vec[mid])
                r = mid - 1;
            else
                l = mid + 1;
        }
        return false;
    }

    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        int lv = 0;
        int rv = m - 1;
        while (lv <= rv)
        {
            int midv = (lv + rv) / 2;
            if (matrix[midv][0] <= target && target <= matrix[midv][n - 1])
            {
                return this->binarySearch(matrix[midv], target);
            }
            else if (matrix[midv][n - 1] < target)
            {
                lv = midv + 1;
            }
            else
            {
                rv = midv - 1;
            }
        }
        return false;
    }
};

int main()
{
    Solution *soln = new Solution();
    vector<vector<int>> matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    bool result = soln->searchMatrix(matrix, 11);
    cout << result << endl;
}
