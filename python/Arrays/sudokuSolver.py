from typing import List
import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)

        boxes = collections.defaultdict(set)  # key (i // 3, j // 3)
        for i in range(0, 9):
            for j in range(0, 9):
                curr = board[i][j]
                if not (ord("0") <= ord(curr) and ord(curr) <= ord("9")):
                    continue

                if curr in cols[j] or curr in rows[i]:
                    return False
                cols[j].add(curr)
                rows[i].add(curr)
                k1 = i // 3
                k2 = j // 3
                if curr in boxes[k1, k2]:
                    return False
                boxes[k1, k2].add(curr)
        return True


soln = Solution()
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(soln.isValidSudoku(board))
