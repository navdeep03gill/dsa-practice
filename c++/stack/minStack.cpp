#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

class MinStack
{
public:
    vector<int> stack;
    vector<int> stackDesc;
    MinStack()
    {
    }

    void push(int val)
    {
        stack.push_back(val);
        if (stackDesc.size() == 0 || val <= stackDesc[stackDesc.size() - 1])
        {
            stackDesc.push_back(val);
        }
    }

    void pop()
    {
        if (stack.size() == 0)
        {
            return;
        }
        int lastElement = stack[stack.size() - 1];
        stack.erase(stack.begin() + (stack.size() - 1));
        if (lastElement == stackDesc[stackDesc.size() - 1])
        {
            stackDesc.erase(stackDesc.begin() + (stackDesc.size() - 1));
        }
        return;
    }

    int top()
    {
        if (stack.size() == 0)
        {
            return 0;
        }
        return stack[stack.size() - 1];
    }

    int getMin()
    {
        return stackDesc[stackDesc.size() - 1];
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

int main()
{
    MinStack *obj = new MinStack();
    obj->push(-2);
    obj->push(0);
    obj->push(-3);
    cout << obj->getMin() << endl;
    obj->pop();
    cout << obj->top() << endl;
    cout << obj->getMin() << endl;
    /*
    MinStack stack = MinStack();
    stack.push(-2);
    stack.push(0);
    stack.push(-3);
    cout << stack.getMin() << endl;
    stack.pop();
    stack.top();
    cout << stack.getMin() << endl;
    */
    return 0;
}
