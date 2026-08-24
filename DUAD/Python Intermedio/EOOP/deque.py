class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.left = None
        self.right = None
    
    def push_right(self, value):
        new_node = Node(value)
        if self.right is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
    
    def push_left(self, value):
        new_node = Node(value)
        if self.left is None:
            self.left = new_node
            self.right = new_node
        else:
            new_node.next = self.left
            self.left.prev = new_node
            self.left = new_node
    
    def pop_right(self):
        if self.right is None:
            print("Deque is empty")
            return None
        removed = self.right
        self.right = self.right.prev
        if self.right is None:
            self.left = None
        else:
            self.right.next = None
        return removed.value
    
    def pop_left(self):
        if self.left is None:
            print("Deque is empty")
            return None
        removed = self.left
        self.left = self.left.next
        if self.left is None:
            self.right = None
        else:
            self.left.prev = None
        return removed.value
    
    def print_deque(self):
        current = self.left
        while current is not None:
            print(current.value)
            current = current.next


# --- Tests ---
deque = Deque()
deque.push_right(2)      # [2]
deque.push_right(3)      # [2, 3]
deque.push_left(1)       # [1, 2, 3]

print("Deque:")
deque.print_deque()

print("Pop right:", deque.pop_right())   # quita 3
print("Pop left:", deque.pop_left())     # quita 1

print("Deque after pops:")
deque.print_deque()