#two-sum hashmap solution 
# reduces lookup time from O(n) to O(1)

from typing import List

class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def soln2(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNums:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        proxy = ListNode()
        curr = proxy
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            L1Val = l1.val if l1 else 0
            L2Val = l2.val if l2 else 0
            presum = L1Val + L2Val + carry
            digit = presum % 10
            carry = presum // 10
            newNode = ListNode(digit)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return proxy.next


class LongestSubstringNRP:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res    

class FindMedianSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = 0
        i2 = 0
        nums3 = []
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 >= len(nums1):
                nums3.append(nums2[i2])
                i2 += 1
            elif i2 >= len(nums2):
                nums3.append(nums1[i1])
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                nums3.append(nums1[i1])
                i1 += 1
            elif nums1[i1] >= nums2[i2]:
                nums3.append(nums2[i2])
                i2 += 1
        
        medi = len(nums3) // 2
        if (len(nums3) % 2 == 0):
            return ((nums3[medi - 1] + nums3[medi]) / 2)
        else:
            return nums3[medi]    



# ADD c, Join c, SWAP c d, NOTHING, IMPOSSIBLE:
def solution(S, T):
    # Implement your solution here
    if S == T:
        return "NOTHING"
    #add -> need T = S+1
    if (len(T) == (len(S) + 1)):
        isAdd = True
        for i in range(len(S)):
            if (S[i] != T[i]):
                isAdd = False
                break
        if isAdd is True:
            toret = "ADD " + T[-1]
            return toret
        else:
            return "IMPOSSIBLE"

    #Join -> need len(S) == len(T) + 1
    elif (len(S) == (len(T) + 1)):
        #find the first point where neq
        idx = 0
        while(True):
            if idx == len(T):
                break
            elif (S[idx] != T[idx]):
                break
            idx += 1
        newS = ""
        if (S[idx] == S[idx - 1]):
            newS = S[:idx] + S[idx+1:]
        # elif idx == len(T):
        #     if (S[idx] == S[idx + 1]):
        #         newS = S[:idx] + S[idx+1:]
        #         print(newS)
        if newS == T:
            return "JOIN " + S[idx]

    #SWAP
    elif len(S) == len(T):
        firstS = 0
        secondS = 0
        diffcount = 0
        for i in range(len(S)):
            if S[i] != T[i]:
                if diffcount == 0:
                    firstS = i
                else:
                    secondS = i
                diffcount += 1
            if diffcount > 2:
                return "IMPOSSIBLE"
        
        newS = S[:firstS] + S[secondS] + S[firstS + 1: secondS] + S[firstS] + S[secondS + 1:]
        if newS == T:
            return "SWAP " + S[firstS] + " " + S[secondS]

        
    return "IMPOSSIBLE"