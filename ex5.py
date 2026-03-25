import random
import timeit

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListPriorityQueue:
    def __init__(self):
        self.head = None

    # insert in sorted order
    def enqueue(self, value):
        new_node = ListNode(value)

        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value < value:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # remove smallest
    def dequeue(self):
        if self.head is None:
            return None

        value = self.head.value
        self.head = self.head.next
        return value


class HeapPriorityQueue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
        self._heapify_up(len(self.data) - 1)

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


# generate tasks
tasks = []
for _ in range(1000):
    if random.random() < 0.7:
        tasks.append(("enqueue", random.randint(1, 1000)))
    else:
        tasks.append(("dequeue", None))


# list PQ test
def run_list():
    list_pq = ListPriorityQueue()
    for task in tasks:
        if task[0] == "enqueue":
            list_pq.enqueue(task[1])
        else:
            list_pq.dequeue()

total_list = timeit.timeit(run_list, number=10)
avg_list = total_list / 10


# heap PQ test
def run_heap():
    heap_pq = HeapPriorityQueue()
    for task in tasks:
        if task[0] == "enqueue":
            heap_pq.enqueue(task[1])
        else:
            heap_pq.dequeue()

total_heap = timeit.timeit(run_heap, number=10)
avg_heap = total_heap / 10


print(f"List PQ - Avg: {avg_list:.6f}s, Total: {total_list:.6f}s")
print(f"Heap PQ - Avg: {avg_heap:.6f}s, Total: {total_heap:.6f}s")


"""
Heap is faster because insert and delete are O(log n).
List insert is O(n) since we must find the correct position.
"""