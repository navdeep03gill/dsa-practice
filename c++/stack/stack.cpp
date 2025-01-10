#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

class Stack
{
    int top;

public:
    int a[INT_MAX];
    Stack() { top = -1; }
    bool push(int x);
    int pop();
    int peek();
    bool isEmpty();
};

bool Stack::push(int x)
{
    if (top >= (INT_MAX - 1))
    {
        cout << "Stack Overflow";
        return false;
    }
    else
    {
        a[++top] = x;
        cout << x << " pushed into stack at index " << top << endl;
        return true;
    }
}

int Stack::pop()
{
    if (top < 0)
    {
        cout << "stack underflow";
        return 0;
    }
    else
    {
        int x = a[top--];
        return x;
    }
}

int Stack::peek()
{
    if (top < 0)
    {
        cout << "Stack is Empty";
        return 0;
    }
    else
    {
        int x = a[top];
        return x;
    }
}

bool Stack::isEmpty()
{
    if (top < 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}
