#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *createLinkedList(vector<int> list)
{
    ListNode *head = new ListNode(list[0]);
    ListNode *tmp = head;
    for (int i = 1; i < list.size(); ++i)
    {
        ListNode *newNode = new ListNode(list[i]);
        tmp->next = newNode;
        tmp = tmp->next;
    }
    return head;
}

void printLinkedList(ListNode *head)
{
    if (!head)
    {
        return;
    }
    ListNode *tmp = head;
    cout << "Printing Linked List ..." << endl;
    cout << "[";
    while (tmp)
    {
        if (!tmp->next)
        {
            cout << tmp->val;
            break;
        }
        cout << tmp->val << ", ";
        tmp = tmp->next;
    }
    cout << "]" << endl;
}

class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return head;
        }
        ListNode *curr = head;
        ListNode *prev = nullptr;
        while (head)
        {
            head = head->next;
            curr->next = prev;
            prev = curr;
            curr = head;
        }
        return prev;
    }

    ListNode *reverseKGroup(ListNode *head, int k)
    {
        if (k == 1)
        {
            return head;
        }
        ListNode *toret = new ListNode(-1);
        toret->next = head;

        ListNode *prevNode = toret;

        while (true)
        {
            ListNode *startNode = prevNode->next;
            ListNode *endNode = startNode;
            int i = k - 1;
            bool toBreak = false;
            while (i > 0 && endNode)
            {
                if (endNode->next == nullptr)
                {
                    toBreak = true;
                    break;
                }
                endNode = endNode->next;
                i -= 1;
            }
            if (i > 0)
                break;
            ListNode *nextNode = nullptr;
            if (endNode->next)
            {
                nextNode = endNode->next;
            }
            endNode->next = nullptr;
            ListNode *revRes = this->reverseList(startNode);
            startNode = revRes;
            endNode = startNode;
            prevNode->next = startNode;
            if (toBreak)
                break;
            i = k - 1;
            while (i > 0)
            {
                endNode = endNode->next;
                i -= 1;
            }
            if (endNode == nullptr)
                break;
            endNode->next = nextNode;
            prevNode = endNode;
        }
        return toret->next;
    }
};

int main()
{
    Solution soln = Solution();
    vector<int> ex1 = {1, 2, 3, 4, 5};
    ListNode *head1 = createLinkedList(ex1);
    printLinkedList(head1);
    ListNode *res1 = soln.reverseKGroup(head1, 2);
    printLinkedList(res1);

    ListNode *head2 = createLinkedList(ex1);
    ListNode *res2 = soln.reverseKGroup(head2, 1);
    printLinkedList(res2);
    return 0;
}
