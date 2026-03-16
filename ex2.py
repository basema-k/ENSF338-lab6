class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key>root.data:
        return search(root.right, key)
        
    return search(root.right, key)
    
    