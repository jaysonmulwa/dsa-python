"""
Stacks and Queues
========================
Stacks and queues are fundamental data structures used to store and manage collections of elements. They are widely used in computer science for various applications, including algorithm design, memory management, and task scheduling.

Stacks
========================
A stack is a linear data structure that follows the Last In First Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. Stacks are often used for function call management, expression evaluation, and backtracking algorithms.
Common operations on stacks include:
- Push: Add an element to the top of the stack.
- Pop: Remove and return the top element of the stack.
- Peek: Return the top element of the stack without removing it.
- IsEmpty: Check if the stack is empty.

Queues
========================
A queue is a linear data structure that follows the First In First Out (FIFO) principle, meaning that the first element added to the queue is the first one to be removed. Queues are commonly used in task scheduling, breadth-first search algorithms, and resource management.
Common operations on queues include:
- Enqueue: Add an element to the end of the queue.
- Dequeue: Remove and return the front element of the queue.
- Peek: Return the front element of the queue without removing it.
- IsEmpty: Check if the queue is empty.

Priority Queues
========================
A priority queue is a special type of queue where each element has a priority associated with it. Elements with higher priority are dequeued before elements with lower priority, regardless of their order in the queue. Priority queues are often implemented using heaps and are used in scheduling algorithms, Dijkstra's algorithm, and Huffman coding.
========================

"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1], reverse=True)
        # Ensure the highest priority is at the front

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[0]
            # Return the item with the highest priority
        raise IndexError("dequeue from empty priority queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0][0]
        raise IndexError("peek from empty priority queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)