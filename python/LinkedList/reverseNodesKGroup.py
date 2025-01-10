# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        if not head:
            return head
        prev = None
        curr = head
        while head is not None:
            head = head.next
            curr.next = prev
            prev = curr
            curr = head
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        toret = ListNode(-1)
        toret.next = head
        prevNode = toret

        while True:
            startNode = prevNode.next
            endNode = startNode
            i = k - 1 
            while i > 0:
                if endNode.next is None:
                    break
                endNode = endNode.next
                i -= 1
            if i > 0:
                break
            toBreak = False
            if endNode.next is None:
                toBreak = True
            nextNode = endNode.next
            endNode.next = None
            newRev = self.reverseList(startNode)
            startNode = newRev
            endNode = startNode
            prevNode.next = startNode
            i = k - 1
            while i > 0:
                if endNode.next is None:
                    break
                endNode = endNode.next
                i -= 1
            endNode.next = None if nextNode is None else nextNode
            prevNode = endNode
            if toBreak: break

        return toret.next


    