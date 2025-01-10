#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> tmp = {"hello"};
    tmp.emplace_back("world");
    cout << "Hello World!" << endl;
    return 0;
}
