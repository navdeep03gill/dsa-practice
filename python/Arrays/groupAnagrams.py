from typing import List
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make an array of all the groups thus far
        groups = defaultdict(list) # mapping char count of each string to list of anagrams
        toret = []
        iterator = 0
        for i in strs:
            count = [0] * 26 # a ... z
            for c in i:
                count[ord(c) - ord("a")] += 1   
            groups[tuple(count)].append(i)
        return groups.values()                    
    def slowGroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make an array of all the groups thus far
        groups = {}
        toret = []
        iterator = 0
        for i in strs:
            letters = {}
            for k in range(len(i)):
                if i[k] not in letters:
                    letters[i[k]] = 1
                else:
                    letters[i[k]] += 1
            matching = False
            for j in range(0, len(groups)):
                if letters == groups[j]:
                    matching = True
                compare = groups[j]
                if len(letters) != len(compare):
                    continue
                ptr = 0 
                for k in letters:
                    if k not in compare:
                        break
                    if letters[k] != compare[k]:
                        break
                    if (ptr == len(letters) - 1):
                        matching = True
                        break
                    ptr += 1
                if matching == True:
                    toret[j].append(i)
                    break            
            # if theres no entry matching, make new group
            if matching == False:
                groups[iterator] = letters
                toret.append([i])
                iterator += 1
        return toret



