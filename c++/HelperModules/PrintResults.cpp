#include "PrintResults.hpp"
 
using namespace std;

namespace PrintFunctions{
    void printVec(vector<int> &vec){
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

    void print2DVector(vector<vector<int>> &vec){
        cout << "[" << endl;
        for (int x = 0; x < vec.size(); ++x)
        {
            vector<int> currVec = vec[x];
            for (int y = 0; y < currVec.size(); ++y)
            {
                int item = currVec[y];
                if (y == currVec.size() - 1)
                    cout << item;
                else
                    cout << item << ", ";
            }
            if (x == vec.size() - 1)
                cout << "]" << endl;
            else
                cout << "]," << endl;
        }
        cout << "]" << endl;
    }
}


/*
template <typename Type>
void Printer::printVec(vector<Type> &vec){
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

template <typename Type>
void Printer::printVectorVector(vector<vector<Type>> &vec){
    cout << "[" << endl;
    for (int x = 0; x < vec.size(); ++x)
    {
        vector<Type> currVec = vec[x];
        for (int y = 0; y < currVec.size(); ++y)
        {
            Type item = currVec[y];
            if (y == currVec.size() - 1)
                cout << item;
            else
                cout << item << ", ";
        }
        if (x == vec.size() - 1)
            cout << "]" << endl;
        else
            cout << "]," << endl;
    }
    cout << "]" << endl;
}
*/
