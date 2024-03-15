class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.size

    def push(self):
        if self.is_full():
            print("Stack is Full!!!!")
        if not self.is_full():
            item = int(input("Enter the element:"))
            self.stack.append(item)
            print(item, "is added to the Stack!")

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!!!")
        if not self.is_empty():
            print(f"Popped Element: {self.stack.pop()}")

    def peek(self):
        if self.is_empty():
            print("Stack is Empty!!!")
        if not self.is_empty():
            print(f"Top element:{self.stack[-1]}")

    def __str__(self):
        if self.is_empty():
            return "Stack is Empty!!!"
        return str(self.stack)


# driver function
def main():
    size = int(input("Enter the size of Stack:"))
    stack = Stack(size)
    while True:
        print("Select the Operation:\n1.Push\t2.Pop\t3.Peek\t4.Display\t5.Quit")
        choice = int(input())
        if choice == 1:
            stack.push()
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            print("Stack:", stack)
        elif choice == 5:
            break
        else:
            print("Invalid Option!!!")


# test cases
main()
