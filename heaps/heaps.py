'''

- binary heap (splits in two at each node) where the parent node is larger than the children node
- note that after preforming an action and heapifying we may go from a representation that looked like this:

[120, 110, 100, 90, 80, 50, 10]

to one that looks like this:

[120, 110, 90, 80, 100, 10]

the first observation may be that 90 and 80 are closer to the first position (assume we are using a max heap and the
first position is the largest item) while 100 is further away. However, the current state would still be correct because
the parent of 100 is 110 and 110 is larger than 100. In turn the heap went from this:

            120
           /   \
         110   100
        /  \   /  \
       90  80 50  10

to:

            120
           /   \
         110   90
        /  \   /
       80 100 10

the main idea is that the first value (i.e 120 for a max heap) is the largest/smallest value. They are mainly good for
finding the largest/smallest value within a dataset.
'''


class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return int((i - 1) / 2)  # get you the index of a parent for another given index

    def left(self, i):
        return self.heap[2 * i + 1]

    def right(self, i):
        return self.heap[2 * i + 2]

    def insert_key(self, v):
        self.heap.append(v)
        self.heapify(len(self.heap) - 1)

    def pop(self):
        result = self.heap.pop(0)
        self.reset()
        return result

    def reset(self):
        for x in range(len(self.heap) - 1):
            self.heapify(x)

    def __repr__(self):
        return f'heap: {self.heap}'

    def heapify(self, i):
        pass

    def delete_key(self, i):
        pass


# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#
#     def parent(self, i):
#         return int((i - 1) / 2)  # get you the index of a parent for another given index
#
#     def left(self, i):
#         return self.heap[2 * i + 1]
#
#     def right(self, i):
#         return self.heap[2 * i + 2]
#
#     def insert_key(self, v):
#         self.heap.append(v)
#         self.heapify(len(self.heap) - 1)
#
#     def delete_key(self, i):
#         self.heap[i] = float('inf')
#         self.heapify(i)
#         self.pop()
#         self.reset()
#
#     def pop(self):
#         self.heap.pop(0)
#
#     def heapify(self, i):
#         while (i != 0 and self.heap[self.parent(i)] < self.heap[i]):
#             self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
#             i = self.parent(i)
#
#     def reset(self):
#         for x in range(len(self.heap) - 1):
#             self.heapify(x)
#
#     def __repr__(self):
#         return f'heap: {self.heap}'
#
#
# class MinHeap:
#     def __init__(self):
#         self.heap = []
#
#     def parent(self, i):
#         return int((i - 1) / 2)  # get you the index of a parent for another given index
#
#     def left(self, i):
#         return self.heap[2 * i + 1]
#
#     def right(self, i):
#         return self.heap[2 * i + 2]
#
#     def insert_key(self, v):
#         self.heap.append(v)
#         self.heapify(len(self.heap) - 1)
#
#     def delete_key(self, i):
#         self.heap[i] = float('-inf')
#         self.heapify(i)
#         self.pop()
#
#     def pop(self):
#         self.heap.pop(0)
#
#     def heapify(self, i):
#         while i != 0 and (self.heap[i] < self.heap[self.parent(i)]):
#             self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
#             i = self.parent(i)
#
#     def __repr__(self):
#         return f'heap: {self.heap}'

class MaxHeap(Heap):
    def __init__(self):
        super().__init__()

    def delete_key(self, i):
        self.heap[i] = float('inf')
        self.heapify(i)
        self.pop()
        self.reset()

    def heapify(self, i):
        while i != 0 and (self.heap[self.parent(i)] < self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def delete_key(self, i):
        self.heap[i] = float('-inf')
        self.heapify(i)
        self.pop()
        self.reset()

    def heapify(self, i):
        while i != 0 and (self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


if __name__ == '__main__':
    max_h = MaxHeap()

    max_h.insert_key(100)
    max_h.insert_key(90)
    max_h.insert_key(110)
    max_h.insert_key(120)
    max_h.insert_key(80)
    max_h.insert_key(50)
    max_h.insert_key(10)

    i = 1
    print(max_h)
    print(f'index {i}: {max_h.heap[i]} left: {max_h.left(i)} right: {max_h.right(i)})')
    max_h.delete_key(5)
    print(max_h)
    print(f'index {i}: {max_h.heap[i]} left: {max_h.left(i)} right: {max_h.right(i)})')

    print('*' * 200)
    min_h = MinHeap()
    min_h.insert_key(100)
    min_h.insert_key(90)
    min_h.insert_key(110)
    min_h.insert_key(120)
    print(min_h)
    min_h.delete_key(2)
    print(min_h)
