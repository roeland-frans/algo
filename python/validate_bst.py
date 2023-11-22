class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    stack = [(tree, float("-inf"), float("+inf"))]
    
    while stack:
        node, minValue, maxValue = stack.pop()
        if node.value < minValue or node.value >= maxValue:
            return False
        if node.left:
            stack.append((node.left, minValue, node.value))
        if node.right:
            stack.append((node.right, node.value, maxValue))

    return True
        

