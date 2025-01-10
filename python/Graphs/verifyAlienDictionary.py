from typing import List

words = [["word", "world", "row"], ["hello", "leetcode"]]
alpha = ["worldabcefghijkmnpqstuvxyz", "hlabcdefgijkmnopqrstuvwxyz"]


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        largestWord = 0
        for i in range(0, len(words)):
            if len(words[i]) > largestWord:
                largestWord = len(words[i])
        wordMatrix = [[""] * largestWord for i in range(0, len(words))]
        for i in range(0, len(words)):
            word = words[i]
            for j in range(len(word)):
                wordMatrix[i][j] = word[j]
        print(wordMatrix)
        priorityMap = {}
        for i in range(0, len(order)):
            priorityMap[order[i]] = i + 1
        print(priorityMap)
        ties = [1] * len(words)

        for j in range(0, largestWord):
            for i in range(1, len(words)):
                if ties[i - 1] == 0:
                    continue
                if wordMatrix[i][j] == "":
                    if wordMatrix[i - 1][j] != "":
                        return False
                    continue
                elif wordMatrix[i - 1][j] == "":
                    ties[i - 1] = 0
                    continue
                if priorityMap[wordMatrix[i][j]] < priorityMap[wordMatrix[i - 1][j]]:
                    return False
                elif priorityMap[wordMatrix[i][j]] > priorityMap[wordMatrix[i - 1][j]]:
                    ties[i - 1] = 0
            done = 1
            for i in range(0, len(words) - 1):
                if ties[i] == 1:
                    done = 0
                    break
            if done:
                return True
        return True


soln = Solution()
toret = soln.isAlienSorted(words[1], alpha[1])
print(toret)
