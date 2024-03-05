def preorder(node):
    print(node, end='')
    if tree[node][0] == '.':
        pass
    else:
        preorder(tree[node][0])
    if tree[node][1] == '.':
        pass
    else:
        preorder(tree[node][1])


def inorder(node):
    if tree[node][0] == '.':
        pass
    else:
        inorder(tree[node][0])
    print(node, end='')
    if tree[node][1] == '.':
        pass
    else:
        inorder(tree[node][1])


def postorder(node):
    if tree[node][0] == '.':
        pass
    else:
        postorder(tree[node][0])
    if tree[node][1] == '.':
        pass
    else:
        postorder(tree[node][1])
    print(node, end='')


N = int(input()) # 이진 트리 노드 개수
tree = {}
for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')


