class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        removed = self.top
        self.top = self.top.next
        return removed.value
    
    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next


# --- Tests ---
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack after pushing 1, 2, 3:")
stack.print_stack()

print("Popped:", stack.pop())

print("Stack after pop:")
stack.print_stack()