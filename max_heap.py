class MaxHeap:
    # Max Heap implementation using array.

    def __init__(self):
        self.heap = []

    def get_max(self):
        # Return the maximum element (root).
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]

    def insert(self, value):
        # Insert a new value into the heap.
        self.heap.append(value)
        self.up_heapify(len(self.heap) - 1)

    def extract_max(self):
        # Remove and return the maximum element.
        if not self.heap:
            raise Exception("Heap is empty")

        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self.down_heapify(0)

        return max_value

    def up_heapify(self, index):
        # Restore heap property upward.
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def down_heapify(self, index):
        # Restore heap property downward.
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
