"""A dynamic array built from scratch, to see how Python's list works internally.

We only use a fixed-size block of memory (a plain list pre-filled with None)
and implement growth ourselves.
"""


class DynamicArray:
    def __init__(self, capacity=2):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity  # fixed-size "raw memory"

    def __len__(self):
        return self._size

    def __getitem__(self, i):  # O(1)
        self._check_index(i)
        return self._data[i]

    def __setitem__(self, i, value):  # O(1)
        self._check_index(i)
        self._data[i] = value

    def __repr__(self):
        return "[" + ", ".join(repr(self._data[i]) for i in range(self._size)) + "]"

    def append(self, value):  # O(1) amortized, O(n) when resizing
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):  # O(n): shift right
        if not 0 <= index <= self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def pop(self, index=None):  # O(1) at end, O(n) elsewhere: shift left
        if self._size == 0:
            raise IndexError("pop from empty array")
        if index is None:
            index = self._size - 1
        self._check_index(index)
        value = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        self._data[self._size] = None  # release reference
        return value

    def index(self, value):  # O(n): linear search
        for i in range(self._size):
            if self._data[i] == value:
                return i
        raise ValueError(f"{value!r} not in array")

    def _resize(self, new_capacity):  # O(n): copy everything
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def _check_index(self, i):
        if not 0 <= i < self._size:
            raise IndexError("index out of range")


if __name__ == "__main__":
    arr = DynamicArray()
    for n in range(1, 9):
        arr.append(n * 10)
        print(f"append {n * 10:>3} -> size={len(arr)} capacity={arr._capacity}")

    arr.insert(0, 5)
    print("after insert(0, 5):", arr)
    print("pop():", arr.pop(), "->", arr)
    print("pop(0):", arr.pop(0), "->", arr)
    print("index(40):", arr.index(40))
    arr[1] = 999
    print("after arr[1] = 999:", arr)

    # Watch the capacity double: 2 -> 4 -> 8 -> 16. Resizes are rare,
    # which is why append is O(1) amortized.
