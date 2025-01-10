from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev = None
        curr = head
        while head is not None:
            head = head.next
            curr.next = prev 
            prev = curr
            curr = head
        return prev

    def revRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        newHead = head
        if head.next:
            newHead = self.revRecursive(head.next)
            head.next.next = head
        head.next = None
        return newHead

def createListNode(arr):
    if not arr: return None
    head = ListNode(arr[0])
    prev = head
    for i in range(1, len(arr)):
        curr = ListNode(arr[i])
        prev.next = curr
        prev = curr 
    return head

def printListNode(head):
    tmp = head
    arr = []
    while tmp:
        arr.append(tmp.val)
        tmp = tmp.next
    print(arr)
    return arr

soln2 = Solution()
inp = createListNode([1,2,3,4,5])
printListNode(inp)
reversedInp = soln2.revRecursive(inp)
printListNode(reversedInp)

