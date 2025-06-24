tree = {}
n = int(input())

for i in range(n):
    parent, left, right = input().split()
    tree[parent] = [left,right] 

def preorder(node):
    if node == '.':
        return
    
    print(node, end='')

    left_child = tree[node][0]
    preorder(left_child)

    right_child = tree[node][1]
    preorder(right_child)

def inorder(node):
    if node == '.':
        return

    left_child = tree[node][0]
    inorder(left_child)
    
    print(node, end='')

    right_child = tree[node][1]
    inorder(right_child)

def postorder(node):
    if node == '.':
        return

    left_child = tree[node][0]
    postorder(left_child)

    right_child = tree[node][1]
    postorder(right_child)

    print(node, end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')