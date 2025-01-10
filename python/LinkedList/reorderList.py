from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printListNode(self, head):
        tmp = head
        arr = []
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        print(arr)
        return arr
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
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        endOfSlow = slow
        endOfSlow.next = None
        reverse = self.reverseList(list2)
        start = head 
        while start and reverse:
            tmp1 = start.next
            tmp2 = reverse.next 
            start.next = reverse
            reverse.next = tmp1
            start = tmp1
            reverse = tmp2

"""
Use fast and slow method to find the second half of list.
Reverse that list. Cut head in half by removing its second half.
Use temp pointers 1 and 2 to intuitively rearrange the lists until 
start and reverse are None.
"""
