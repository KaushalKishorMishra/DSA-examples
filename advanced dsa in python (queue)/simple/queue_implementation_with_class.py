# class implementation of queue data structure
class Queue:
    # Queue class constructor
    def __init__(self, size):
        # initialize the queue with None values for the given size
        self.queue = [None] * size
        # set the size of the queue
        self.size = size
        # set the front and rear to -1
        self.front = self.rear = -1

    # check if the queue is empty
    def is_empty(self):
        return self.front == self.rear == -1

    # check if the queue is full
    def is_full(self):
        return self.rear == self.size - 1

    # add an element to the rear of the queue
    def enqueue(self):
        if self.is_full():
            print("Queue is Full!!!!")
        else:
            element = input("Enter the element:")
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear += 1
            self.queue[self.rear] = element
            print(element, "is added to the Queue!")

    # remove an element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!!!")
        else:
            e = self.queue[self.front]
            print("Element removed!!:", e)
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1

    # display the queue elements
    def display(self):
        if self.is_empty():
            print("Queue is Empty!!!")
        else:
            print("Queue:", self.queue[self.front:self.rear + 1])

    # peek the front element of the queue
    def peek(self):
        if self.is_empty():
            print("Queue is Empty!!!")
        else:
            print("Front element is:", self.queue[self.front])

# driver function
def main():
    # take the size of the queue from the user
    size = int(input("Enter the size of Queue: "))
    # create a queue object
    queue = Queue(size)
    while True:
        print("Select the Operation:\n1.Add\t2.Delete\t3. Display\t4. Peek\t5. Quit")
        choice = int(input())
        # perform the operation based on the user choice
        if choice == 1:
            queue.enqueue()
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            queue.peek()
        elif choice == 5:
            break
        else:
            print("Invalid Option!!!")

# driver function call
main()
