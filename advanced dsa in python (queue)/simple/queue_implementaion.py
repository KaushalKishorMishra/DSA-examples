# Implement Queue using List(Functions)
q = []


def is_empty():
    if len(q) == 0:
        return True
    else:
        return False


def Enqueue(size):
    if len(q) == size:  # check wether the stack is full or not
        print("Queue is Full!!!!")
    else:
        element = input("Enter the element:")
        q.append(element)
        print(element, "is added to the Queue!")


def dequeue():
    if is_empty():  # or if len(stack)==0
        print("Queue is Empty!!!")
    else:
        e = q.pop(0)
        print("element removed!!:", e)


def display():
    if is_empty():
        print("Queue is Empty!!!")
    else:
        print("Queue:", q)


def main():
    size = int(input("Enter the size of Queue: "))
    while True:
        print("Select the Operation:\n1.Add\t2.Delete\t3. Display\t 4. Quit")
        choice = int(input())
        if choice == 1:
            Enqueue(size)
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Invalid Option!!!")


# test cases
main()
