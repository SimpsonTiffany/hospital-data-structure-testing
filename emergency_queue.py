class Patient:
    """
    Represents a patient arriving to the emergency room.
    urgency is an integer from 1 to 10, where 1 is most urgent.
    """

    def __init__(self, name: str, urgency: int):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    """
    Custom min heap to manage emergency intake.
    data[0] is always the most urgent patient, the lowest urgency number.
    """

    def __init__(self):
        self.data = []

    def _parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def _right_child_index(self, index: int) -> int:
        return (2 * index) + 2

    def heapify_up(self, index: int) -> None:
        while index > 0:
            parent = self._parent_index(index)
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = (
                    self.data[parent],
                    self.data[index],
                )
                index = parent
            else:
                break

    def heapify_down(self, index: int) -> None:
        size = len(self.data)
        while True:
            left = self._left_child_index(index)
            right = self._right_child_index(index)
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = (
                    self.data[smallest],
                    self.data[index],
                )
                index = smallest
            else:
                break

    def insert(self, patient: Patient) -> None:
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    def remove_min(self):
        if len(self.data) == 0:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        root = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)
        return root

    def print_heap(self) -> None:
        if len(self.data) == 0:
            print("Current Queue is empty.")
            return

        print("Current Queue:")
        for patient in self.data:
            print(f"{patient.name} ({patient.urgency})")


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()

    print("Edge case test, peek on empty heap:")
    print(heap.peek())

    print("\nEdge case test, remove_min on empty heap:")
    print(heap.remove_min())

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Riley", 2))

    print("\nAfter inserts:")
    heap.print_heap()

    next_up = heap.peek()
    print("\nPeek result:")
    if next_up:
        print(next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("\nRemoved most urgent patient:")
    if served:
        print(served.name, served.urgency)

    print("\nQueue after removal:")
    heap.print_heap()

    print("\nRemove remaining patients until empty:")
    while heap.peek() is not None:
        p = heap.remove_min()
        print(p.name, p.urgency)

    print("\nFinal check, heap should be empty:")
    heap.print_heap()
