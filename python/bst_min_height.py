def minHeightBst(array):
    stack = []
    bst = None
    stack.append((0, len(array) - 1))

    while stack:
        startIdx, endIdx = stack.pop()

        if endIdx < startIdx:
            continue
        
        midIdx = (startIdx + endIdx) // 2
        value = array[midIdx]
        if bst is None:
            bst = BST(value)
        else:
            bst.insert(value)
        stack.append((startIdx, midIdx - 1))
        stack.append((midIdx + 1, endIdx))

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

