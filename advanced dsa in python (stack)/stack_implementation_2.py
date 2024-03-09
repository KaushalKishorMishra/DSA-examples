class Stack:
    def __init__(self, max_size):
        self = []
        self.max_size = max_size  # Set a maximum capacity

    def isEmpty(self):
        return self == []

    def is_full(self):
        return len(self.items) == self.max_size

    def push(self, data):
        if self.is_full():
            print("Stack overflow")
            return
        return self.stack.append(
            data
        )  

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.stack[-1]

        def __str__(self):
            return str(self.stack)


# Example usage
my_stack = Stack(5)  # Create a stack with a maximum size of 5
my_stack.push(5)
my_stack.push(6)
if not my_stack.is_full():
    my_stack.push()
else:
    print("Stack is full, cannot push more elements")

print(my_stack.pop())
print(my_stack.peek())
