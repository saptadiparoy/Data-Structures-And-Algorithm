#making a fixed size stack in python

class fixedstack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = [None]* capacity
        self.top = -1

    def isempty(self) -> bool:
        return self.top == -1

    def isfull(self) -> bool:
        return self.top == self.capacity -1

    #push
    def push(self, item):
        if self.isfull():
            print ("Stack overflow!")

        else:
            self.top += 1 #increment the top pointer
            self.stack[self.top] = item #change the top to now be inserted element

    #pop
    def pop(self):
        if self.isempty():
            print ("Stack Underflow!")

        else:
            item = self.stack[self.top] #assign the top item to some other variable/placeholder
            self.stack[self.top] = None #change the top to none
            self.top -= 1 #decrement the top pointer
            return item #return the previous top item which is now popped

    def peek(self):
        if self.isempty():
            print ("Stack is empty!")

        else:
            print ("Top element is  :   ", self.stack[self.top])

    def display(self):
        if self.isempty():
            print ("Stack is empty!")

        else:
            active_elements = self.stack [:self.top +1] #sliced to remove "none"/empty slots
            print ("your Stack  :")
            for i in reversed(active_elements): #puts the list in reverse to get bottom to top print vertically
                print (i)

if  __name__ == "__main__":
    capacity = int(input("Enter stack capacity  :"))
    stack = fixedstack(capacity)

    while True:
        print ("----Stack Menu----")
        print ("1.Push \n2.Pop \n3.Peek \n4.Display \n5.Exit")

        choice = int(input("Enter your choice   :"))

        if choice == 1:
            item = (input("Enter element to push    :"))
            stack.push(item)

        elif choice == 2:
            popped = stack.pop()

            print ("Item popped :", popped)

        elif choice == 3:
            stack.peek()

        elif choice == 4:
            stack.display()

        elif choice == 5:
            print("Byee!!")
            break

        else:
            print("Invalid Try again!")
