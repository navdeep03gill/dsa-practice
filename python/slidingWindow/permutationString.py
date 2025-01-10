class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        matches = 0

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        l = 0
        for j in range(len(s1) ,len(s2)):
            if matches == 26: return True
            index = ord(s2[j]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
        


    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     s1Map = {}
    #     for i in range(len(s1)):
    #         s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
    #     s1MCopy = dict(s1Map)
    #     l = 0
        
    #     for r in range(len(s2)):
    #         if s2[r] not in s1MCopy:
    #             print(s2[r])
    #             s1MCopy = dict(s1Map)
    #         else:
    #             s1MCopy[s2[r]] -= 1
    #             if s1MCopy[s2[r]] == 0:
    #                 del s1MCopy[s2[r]]

    #         print(s1MCopy)
    #         if len(s1MCopy) == 0:
    #             return True
    #     return False
    