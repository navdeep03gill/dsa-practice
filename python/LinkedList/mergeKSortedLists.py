from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printListNode(self):
        tmp = self
        arr = []
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        print(arr)
        return arr

def createListNode(arr):
    if not arr: return None
    head = ListNode(arr[0])
    prev = head
    for i in range(1, len(arr)):
        curr = ListNode(arr[i])
        prev.next = curr
        prev = curr 
    return head

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        d = {}
        for head in lists:
            while(head):
                if head.val not in d:
                    d[head.val] = 1
                else:
                    d[head.val] += 1
                head = head.next
        dKeys = list(d.keys())
        dKeys.sort()
        toret = ListNode(-1)
        tmp = toret
        for value in dKeys:
            i = d[value]
            while i > 0 :
                newNode = ListNode(value)
                tmp.next = newNode
                tmp = tmp.next
                i -= 1
        return toret.next


def runner(inp):
    toPass = []
    for i in inp:
        newHead = createListNode(i)
        toPass.append(newHead)
    soln = Solution()
    result = soln.mergeKLists(toPass)
    result.printListNode()
    

inp1 = [[1,4,5],[1,3,4],[2,6]]
runner(inp1)

        # d=defaultdict(int)
        # for i in lists:
        #     head = ListNode(-1)
        #     head.next = i
        #     head = head.next
        #     while head:
        #         d[head.val] += 1
        #         head = head.next
        # head = ListNode(-1)
        # tmp = head
        # vals = sorted(d.keys(), reverse=True)
        # print(vals)
        # while vals:
        #     k = vals.pop()
        #     for i in range(d[k]):
        #         tmp.next = ListNode(k)
        #         tmp = tmp.next
        # return head.next

        
        