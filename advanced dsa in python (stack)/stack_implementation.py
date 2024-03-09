# stack implementation
class Stack:
    # constructor for the stack class
    def __init__(self):
        self.stack = []

    # method to check wether the stack is empty or not
    def is_empty(self):
        return len(self.stack) == 0

    # method to get the size of the stack
    def size(self):
        return len(self.stack)

    # method to push elements to the stack
    def push(self, data):
        self.stack.append(data)

    # method to pop elements from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    # method to get the top element of the stack
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # method to print the stack
    def __str__(self):
        return str(self.stack)


# create a stack object
stack = Stack()
# checking the size of the stack
print(f"Stack is of size: {stack.size()}")
# pushing elements to the stack
stack.push("Kaushal Kishor Mishra")
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
# checking wether the stack is empty or not
print(f"Stack is empty: {stack.is_empty()}")
# checking the size of the stack
print(f"Stack is of size: {stack.size()}")
# checking the top element of the stack
print(f"Stack peek: {stack.peek()}")
# printing the stack
print(f"Stack: {stack}")
# popping elements from the stack
stack.pop()
print(f"Stack is of size: {stack.size()}")
print(f"Stack peek: {stack.peek()}")
print(f"Stack: {stack}")
stack.pop()
print(f"Stack is of size: {stack.size()}")
print(f"Stack peek: {stack.peek()}")
print(f"Stack: {stack}")
stack.pop()
print(f"Stack is of size: {stack.size()}")
print(f"Stack peek: {stack.peek()}")
print(f"Stack: {stack}")
stack.pop()
print(f"Stack is of size: {stack.size()}")
print(f"Stack peek: {stack.peek()}")
print(f"Stack: {stack}")
