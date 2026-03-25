import random

class Heap:
    def __init__(self):
        self.data = []

    # build heap from array
    def heapify(self, array):
        self.data = array.copy()
        for i in range(len(self.data)//2 - 1, -1, -1):
            self._heapify_down(i)

    # insert element
    def enqueue(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

    # remove smallest element
    def dequeue(self):
        if not self.data:
            return None

        root = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self._heapify_down(0)

        return root

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left

        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self._heapify_down(smallest)


# --------- TESTS ---------

# already heap
heap1 = Heap()
heap1.heapify([1, 3, 5, 7])
print("Test 1:", heap1.data)

# empty array
heap2 = Heap()
heap2.heapify([])
print("Test 2:", heap2.data)

# random array
heap3 = Heap()
random_array = list(range(10))
random.shuffle(random_array)
heap3.heapify(random_array)
print("Test 3:", heap3.data)