# exercise 2

import random
import timeit


# 1:

class TreeNode:
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


# binary search (array)
def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return False


# 2:
n = 10000
arr = list(range(n))
random.shuffle(arr)

# binary search tree
bst = BinarySearchTree()
for value in arr:
    bst.insert(value)

num_trials = 10
bst_total_time = 0

for value in arr:
    elapsed = timeit.timeit(lambda: bst.search(value), number=num_trials)
    bst_total_time += (elapsed / num_trials)

bst_avg_time = bst_total_time / n

print("BST Search Performance:")
print("Average time per search:", bst_avg_time)
print("Total time:", bst_total_time)


# 3:

arr.sort()

bs_total_time = 0

for value in arr:
    elapsed = timeit.timeit(lambda: binary_search(arr, value), number=num_trials)
    bs_total_time += (elapsed / num_trials)

bs_avg_time = bs_total_time / n

print("\nBinary Search Performance:")
print("Average time per search:", bs_avg_time)
print("Total time:", bs_total_time)


# 4:

# In general, binary search on arrays is faster than searching in a BST.
# This is because:
# Binary search operates on a contiguous block of memory (array),
# The BST involves pointer traversal, which is slower in practice.
# Both approaches have O(log n) time complexity on average,
# but constants matter so, binary search is typically faster in practice,
# even though both methods are theoretically efficient.