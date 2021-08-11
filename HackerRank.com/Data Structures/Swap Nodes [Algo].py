from collections import deque

class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.index = index
        
    
def in_order_traverse(root):
    """Don't use recursion b/c of recursion limit."""
    stack = deque([root])
    visited = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.index in visited:
            print(node.index, end=' ')
            continue
        visited.add(node.index)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)
    
    
def swap(root, k):
    """Don't use recursion b/c of recursion limit."""
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.append((node.left, level+1))
        q.append((node.right, level+1))

        
        
# get number of nodes    
N = int(input())

# create node list
nodes = [None]*(N+1)
for i in range(1, N+1):
    n = Node(i)
    n.left_index, n.right_index = [v if v > 0 else 0 for v in map(int, input().split())]
    nodes[i] = n

# fill out node objects
for n in nodes[1:]:
    left = nodes[n.left_index]
    right = nodes[n.right_index]
    n.left = left
    n.right = right

T = int(input())
root = nodes[1]
# do the swapping
for _ in range(T):
    k = int(input())
    swap(root, k)
    in_order_traverse(root)
    print('')
