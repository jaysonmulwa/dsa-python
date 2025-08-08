"""
Linked Lists
========================
Linked lists are a fundamental data structure that consists of a sequence of elements, where each element (node) contains a value and a reference (or pointer) to the next node in the sequence. 
Linked lists are dynamic in nature, allowing for efficient insertion and deletion of elements.
They are widely used in various applications, including memory management, data manipulation, and algorithm design.
Common operations on linked lists include:
- Insertion: Adding a new node to the linked list at a specific position (beginning, end, or middle).
- Deletion: Removing a node from the linked list at a specific position.
- Traversal: Visiting each node in the linked list to access or modify its value.
- Searching: Finding a specific value in the linked list.
Traversal of a linked list has a time complexity of O(n), where n is the number of nodes in the list. 
Insertion and deletion operations can be performed in O(1) time if done at the head of the list, but O(n) if done at a specific position or at the tail.  
"""

from sympy import N


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
            current.next = new_node

    def delete_node(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert_at_head(10)
linked_list.insert_at_tail(20)
linked_list.insert_at_tail(30)
linked_list.traverse()  # Output: 10 -> 20 -> 30 -> None