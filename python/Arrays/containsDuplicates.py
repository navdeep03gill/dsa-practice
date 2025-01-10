from typing import List
import collections
from collections import defaultdict 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for i in nums:
            if i in dups:
                return True
            dups.add(i)
        return False
    

phonebook = {
    "bob": 7387,
    "alice": 3719,
    "jack": 7052,
}

squares = {x: x * x for x in range(6)}

# Ordered Dict preserves the order of insertion of the keys
ordered_d = collections.OrderedDict(one=1, two=2, three=3)

# defaultdict lets you use callable constructor whose return value will be used if a 
# requested key cannot be found
default_d = defaultdict(list)
default_d['dogs'].append('Rufus')
default_d['dogs'].append('Kathrun')


def main():
    nums = [1,2,3,1]
    sol = Solution()
    contains_duplicate = sol.containsDuplicate(nums)
    print(contains_duplicate)
    print('ordered dict:', ordered_d)
    print(ordered_d.keys(), ordered_d.values())
    print('default_d:', default_d['dogs'])
    return 0

if __name__ == "__main__":
    main()
