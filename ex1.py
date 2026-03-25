import random
import timeit

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)


sorted_vector = list(range(10000))
bst1 = BST()
for val in sorted_vector:
    bst1.insert(val)

def search_sorted():
    for val in sorted_vector:
        bst1.search(val)

total_sorted = timeit.timeit(search_sorted, number=10)
avg_sorted = total_sorted / 10
print(f"Sorted - Avg: {avg_sorted:.6f}s, Total: {total_sorted:.6f}s")

shuffled_vector = sorted_vector.copy()
random.shuffle(shuffled_vector)
bst2 = BST()
for val in shuffled_vector:
    bst2.insert(val)

def search_shuffled():
    for val in shuffled_vector:
        bst2.search(val)

time_shuffled = timeit.timeit(search_shuffled, number=10) / 10
print(f"Shuffled insertion - Average time: {time_shuffled:.6f}s, Total time: {time_shuffled*10000:.6f}s")

"""
The shuffled insertion approach is faster. When inserting sorted data, the BST becomes skewed 
(like a linked list) with height O(n), making searches O(n). With shuffled data, the tree is 
more balanced with height O(log n), making searches faster.
"""