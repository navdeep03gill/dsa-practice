from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        toret = ""
        for item in strs:
            k = len(item)
            toret += str(k)
            toret += "#"
            toret += item
        return toret

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 0:
            return []
        toret = []
        arr = list(s)
        i = 0
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            print(count)
            k = int(count)
            i += 1
            newWord = ""
            while k > 0 and i < len(s):
                newWord += s[i]
                k -= 1
                i += 1
            toret.append(newWord)
        return toret
