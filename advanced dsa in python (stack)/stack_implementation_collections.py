from collections import deque

# creating a stack using deque
stack = deque()

# checking the size of the stack
print(f"Stack is of size: {len(stack)}")

# pushing elements to the stack
stack.append("Kaushal Kishor Mishra")

# pushing elements to the stack
stack.append(2)

# pushing elements to the stack
stack.append(3)

# printing the stack
print(f"Stack : {stack}")

# pushing elements to the stack
stack.append(4)

# printing the stack
print(f"Stack : {stack}")

# peeking the top element of the stack
print(f"Peek value:{stack[-1]}")

# popping elements from the stack
print(f"Popped value: {stack.pop()}")

# peeking the top element of the stack
print(f"Peek value:{stack[-1]}")

# popping elements from the stack
print(f"Popped value: {stack.pop()}")

# peeking the top element of the stack
print(f"Peek value:{stack[-1]}")

# popping elements from the stack
print(f"Popped value: {stack.pop()}")

# peeking the top element of the stack
print(f"Peek value:{stack[-1]}")

# printing the stack
print(f"Stack : {stack}")

# popping elements from the stack
# print(f"Popped value: {stack.pop()}")

# deque doesn't have a peek() method, use indexing
print("Top element:", stack[-1] if stack else "Stack is empty")

# deque doesn't have a size() method, use len()
print("Number of elements:", len(stack))

# No is_empty() method, use len() check
print("Is stack empty:", not len(stack))
