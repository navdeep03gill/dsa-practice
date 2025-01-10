# Data Struct that stores 100 million records, perform insertion search, update, and list operations efficiently

import math
from collections import deque
from re import L
from unittest.mock import NonCallableMagicMock
from xml.dom.minicompat import NodeList


class User:
    # constructor
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()
    
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}".format(guest_name, self.name, self.email))


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            if user.username < self.users[i].username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for i in self.users:
            if i.username == username:
                return i
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()

for i in users:
    database.insert(i)

# Limitations: time complexity is terrible
# Insert: O(N), Find: O(N), Update: O(N), List: 0(1)
# Sorted list of users is inefficient data struct for organizing profile info of millions of users

# Binary Search Trees
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def display_keys(self, level=0):
        if self is None:
            print('\t'*level + '∅')
            return
        if self.left is None and self.right is None:
            print('\t'*level + str(self.key))
            return
        TreeNode.display_keys(self.left, level+1)
        print('\t'*level + str(self.key))
        TreeNode.display_keys(self.right, level+1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = parse_tuple(data[0])
            node.right = parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node



node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
node0.left = node1
node0.right = node2

# build bst with tuple
def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree1_tuple = (1, 2, ((None, 3, 4), 5, (6,7,8)))
tree2_tuple = ( (1, 2, (3, 4, None)) , 5, ((6, 7, 8), 9, (((10, 11, None), 12, None), 13, 14)))

tree1 = TreeNode.parse_tuple(tree1_tuple)
tree2 = TreeNode.parse_tuple(tree2_tuple)

#print(tree1.height())


# The minimum depth is the number of nodes along the shortest path 
# from the root node down to the nearest leaf node.

def minDepth(node):
    if node is None:
        return 0
    queue = deque()
    queue.append((node, 1))
    while len(queue) > 0:
        firstnode, firstdepth = queue.popleft()
        if firstnode.left == None and firstnode.right == None:
            return firstdepth
        if firstnode.left != None:
            queue.append((firstnode.left, firstdepth + 1))
        if firstnode.right != None:
            queue.append((firstnode.right, firstdepth + 1))

# print(minDepth(tree1))
# print(minDepth(tree2))

def diameterOfTree(node):
    if node is None:
        return 0
    node_stack = [node]
    max_depth = {}
    max_path = {}
    seen = set()
    while node_stack:
        root = node_stack.pop()

        if root not in seen:
            seen.add(root)
            node_stack.append(root)
            if root.left:
                node_stack.append(root.left)
            if root.right:
                node_stack.append(root.right)
        else:
            if not root.left and not root.right:
                max_depth[root] = 0
                max_path[root] = 0
            elif not root.left and root.right:
                max_right = max_depth[root.right]
                max_depth[root] = max_right + 1
                max_path_right = max_path[root.right]
                max_path[root] = max(max_depth[root], max_path_right)
            elif root.left and not root.right:
                max_left = max_depth[root.left]
                max_depth[root] = max_left + 1
                max_path_left = max_path[root.left]
                max_path[root] = max(max_depth[root], max_path_left)
            else:
                max_left = max_depth[root.left]
                max_right = max_depth[root.right]
                max_depth[root] = max(max_left, max_right) + 1
                max_path[root] = max(max_left + max_right + 2,
                                    max_path[root.left],
                                    max_path[root.right])
    return max_path[node]


#print(diameterOfTree(tree1))
#print(diameterOfTree(tree2))

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_L, min_L, max_L = is_bst(node.left)
    is_bst_R, min_R, max_R = is_bst(node.right)
    is_bst_node = (is_bst_L and is_bst_R and
                    (max_L is None or node.key > max_L) and
                    (max_R is None or node.key < max_R))
    min_key = min(remove_none([min_L, node.key, min_R]))
    max_key = max(remove_none([max_L, node.key, max_R]))

    return is_bst_node, min_key, max_key

# another solid soln for valid bst
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.key < right and node.key > left):
                return False
            return (valid(node.left, left, node.key) and 
                    valid(node.right, node.key, right))
        
        return valid(root, float("-inf"), float("inf"))

    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root):
            if not root: return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            


soln = Solution()

print(soln.isValidBST(tree1))

#Storing Key-Value Pairs in BST
# Pointer to the parent node (for easier upward traversal)

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    else:
        node.right = insert(node.right, key, value)  
        node.right.parent = node      
    return node

dtree = BSTNode('nav.username', 'nav')
dtree.left = BSTNode(jadhesh.username, jadhesh)
dtree.right = BSTNode(sonaksh.username, sonaksh)

insert(dtree, 'pablo.username', 'pablo')

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    elif key < node.key:
        return find(node.left, key)
    else: 
        return find(node.right, key)


def update(node, key, value):
    found = find(node, key)
    found.value = value

def display_keys(node, level=0):
    if node is None:
        print('\t'*level + '∅')
        return
    if node.left is None and node.right is None:
        print('\t'*level + str(node.key))
        return
    display_keys(node.right, level+1)
    print('\t'*level + str(node.key))
    display_keys(node.left, level+1)

display_keys(dtree)

def list_all(node):
    if node is None:
        return []
    return  list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height




