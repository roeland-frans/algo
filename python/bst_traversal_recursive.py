def inOrderTraverse(tree, array):
    def traverse(node, array, parent = None):
        if node.left:
            traverse(node.left, array)
            
        array.append(node.value)
        
        if node.right:
            traverse(node.right, array)

    traverse(tree, array)
    
    return array


def preOrderTraverse(tree, array):
    def traverse(node, array):
        array.append(node.value)
        if node.left:
            traverse(node.left, array)
        if node.right:
            traverse(node.right, array)

    traverse(tree, array)
    
    return array


def postOrderTraverse(tree, array):
    def traverse(node, array):
        if node.left:
            traverse(node.left, array)
        if node.right:
            traverse(node.right, array)
        array.append(node.value)
        
    traverse(tree, array)
    
    return array

