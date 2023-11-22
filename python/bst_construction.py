class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Average: O(log(n)) time | O(log(n)) space
        # Worst: O(n) time | O(n) space
        self._insert(self, value)
        return self
        
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BST(value)
            else:
                self._insert(node.left, value)
        elif value >= node.value:
            if node.right is None:
                node.right = BST(value)
            else:
                self._insert(node.right, value)

    def contains(self, value):
        # Average: O(log(n)) time | O(log(n)) space
        # Worst: O(n) time | O(n) space
        return self._contains(self, value)

    def _contains(self, node, value):
        if value == node.value:
            return True
        if value < node.value:
            if node.left:
                return self._contains(node.left, value)
            else:
                return False
        if value > node.value:
            if node.right:
                return self._contains(node.right, value)
            else:
                return False
                
    def remove(self, value, parent = None):
        # Average: O(log(n)) time | O(1) space
        # Worst: O(n) time | O(1) space
        node = self
        while node:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                if node.left and node.right:
                    node.value = node.right.getMinValue()
                    node.right.remove(node.value, node)
                elif parent is None:
                    if node.left:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                elif parent.left == node:
                    if node.left:
                        parent.left = node.left
                    else:
                        parent.left = node.right
                elif parent.right == node:
                    if node.left:
                        parent.right = node.left
                    else:
                        parent.right = node.right
                break
        return self
                

    def getMinValue(self):
        node = self
        while node.left:
            node = node.left
        return node.value

