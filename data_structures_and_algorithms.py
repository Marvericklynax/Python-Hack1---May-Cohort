# data_structures_and_algorithms.py

# 1. Reverse a String Using a Stack
def reverse_string(s: str) -> str:
    stack = []
    # Push all characters to the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ""
    # Pop characters from the stack
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# 2. Implement a Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int):
        # Push to stack1
        self.stack1.append(x)

    def dequeue(self) -> int:
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Return the top element from stack2 (this is the front of the queue)
        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # In case the queue is empty

# 3. Find the Maximum Element in a List Using a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            return None  # List is empty

        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

# Example usages
if __name__ == "__main__":
    # Test reverse_string
    print(reverse_string("hello"))  # Output: "olleh"

    # Test QueueWithStacks
    q = QueueWithStacks()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2

    # Test LinkedList and find_max
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print(ll.find_max())  # Output: 4
