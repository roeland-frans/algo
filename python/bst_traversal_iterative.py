def inOrderTraverse(tree, array):
    stack = []
    node = tree
    while stack or node:
        # Left side
        while node:
            stack.append(node)
            node = node.left
            
        node = stack.pop()
        array.append(node.value)

        # Process right side
        node = node.right
    return array


def preOrderTraverse(tree, array):
    stack = [tree]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        array.append(node.value)
    return array


def postOrderTraverse(tree, array):
    stack = [tree]
    while stack:
        node = stack.pop()
        array.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return array[::-1]

