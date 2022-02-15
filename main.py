class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def dfs(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        res.append(current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return res


def recursive_dfs(root):
    if not root:
        return []
    left = recursive_dfs(root.left)
    right = recursive_dfs(root.right)
    return [root.value, *left, *right]


def bfs(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        res.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return res


def dfs_includes(root, value):
    if not root:
        return False
    stack = [root]
    while stack:
        current = stack.pop()
        if current.value == value:
            return True
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return False


def dfs_recursive_includes(root, value):
    if not root:
        return False
    if root.value == value:
        return True
    return dfs_recursive_includes(root.left, value) or dfs_recursive_includes(root.right, value)


def tree_sum(root):
    if not root:
        return 0
    stack = [root]
    res = 0
    while stack:
        current = stack.pop()
        res += current.value
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return res


def recursive_tree_sum(root):
    if not root:
        return 0
    return root.value + recursive_tree_sum(root.left) + recursive_tree_sum(root.right)


def min_value(root):
    if not root:
        return float('inf')
    stack = [root]
    res = float('inf')
    while stack:
        current = stack.pop()
        res = min(res, current.value)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return res


def recursive_min_value(root):
    if not root:
        return float('inf')
    return min(root.value, recursive_min_value(root.left), recursive_min_value(root.right))


def recursive_max_root_to_leaf_sum(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.value
    return root.value + max(recursive_max_root_to_leaf_sum(root.left), recursive_max_root_to_leaf_sum(root.right))


assert recursive_max_root_to_leaf_sum(a), 18
assert recursive_min_value(a), -2
assert min_value(a), -2
assert tree_sum(a), 22
assert recursive_tree_sum(a), 22
assert dfs(a), [3, 11, 4, 2, 4, -2]
assert recursive_dfs(a), [3, 11, 4, 2, 4, -2]
assert bfs(a), [3, 11, 4, 4, 2, -2]
assert dfs_includes(a, 1) is False
assert dfs_recursive_includes(a, 2) is True
