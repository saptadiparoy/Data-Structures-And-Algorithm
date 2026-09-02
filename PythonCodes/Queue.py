#creating a fixed size queue using arrays

class fixedqueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.end = 0
        self.size = 0

    def isempty(self) -> bool:
        return self.size == 0

    def isfull(self) -> bool:
        return self.size == self.capacity

    def enqueue(self, item):
        if self.isfull():
            print ("Queue Overflow!!")

        else:
            self.queue[self.end] = item
            self.end += 1
            self.size +=1
            

    def dequeue(self):
        if self.isempty():
            print ("Queue Underflow!!")

        else:
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            self.size -= 1
            return item

    def peek(self):
        if self.isempty():
            print ("Queue is empty! nothing to see.")

        else:
            print ("Front element   :   ", self.queue[self.front])

    def display(self):
        if self.isempty():
            print ("Queue is empty! nothing to see.")

        else:
            active_elements = self.queue[self.front : self.end + 1]
            print ("Your Queue     :   ", active_elements)



if  __name__ == "__main__":
    capacity = int(input("Enter queue capacity  :"))
    queue = fixedqueue(capacity)

    while True:
        print ("----Queue Menu----")
        print ("1.Enqueue \n2.Dequeue \n3.Peek \n4.Display \n5.Exit")

        choice = int(input("Enter your choice   :"))

        if choice == 1:
            item = (input("Enter element to push    :"))
            queue.enqueue(item)

        elif choice == 2:
            popped = queue.dequeue()

            print ("Item popped :", popped)

        elif choice == 3:
            queue.peek()

        elif choice == 4:
            queue.display()

        elif choice == 5:
            print("Byee!!")
            break

        else:
            print("Invalid Try again!")
