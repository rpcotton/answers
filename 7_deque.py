#7. Write a python code to implement a queue using collections.deque (double ended queue)

from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self._queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._queue[0]

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

#main program

# Create a queue
queue = Queue()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue()) # Output: 1
print(queue.dequeue()) # Output: 2

# Peek at the front element
print(queue.peek()) # Output: 3

# Check if the queue is empty
print(queue.is_empty()) # Output: False

# Get the size of the queue
print(queue.size()) # Output: 1