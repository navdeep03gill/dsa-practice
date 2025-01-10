from collections import deque
from typing import List

class Solution:
        
    def simplifyPath(self, path: str) -> str:
        # create stack in one go?
        # path = path.replace('//', '/') # O(n)
        # how to replace without string replace?
        new_path = ""
        for i in range(len(path)):
            if path[i] == '/' and path[i-1] == '/':
                continue
            new_path += path[i]
        path = new_path
        print(new_path)
        path_stack = deque()
        for sub_path in path.split('/'):
            if sub_path:
                if sub_path == "..":
                    if len(path_stack) > 0:
                        path_stack.pop()
                    continue
                if sub_path == ".":
                    continue
                path_stack.append(sub_path)
        toret = ""
        while(True):
            toret += '/'
            if path_stack:
                item = path_stack.popleft()
                toret += item
            if not path_stack:
                break
        return toret
            

def main():
    soln = Solution()
    path = "/home/user/Documents//../Pictures"
    result = soln.simplifyPath(path)
    print(result)
    return result

if __name__ == '__main__':
    main()
