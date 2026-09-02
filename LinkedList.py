#creating a fixed length linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None

    def getsize(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def isempty(self) -> bool:
        return self.head is None

    def isfull(self) -> bool:
        return self.getsize() == self.capacity

    def insert_front(self, data):
        if self.isfull():
            print ("Overflow!")
            return False

        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
        return True

    def insert_end(self, data):
        if self.isfull():
            print ("Overflow!")
            return False
        
        
        new_node = node(data)
        if self.isempty():
            self.head = new_node
            return True

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        return True
        
    def delete(self):
        if self.isempty():
            print("List is Empty! nothing to see.")
            return None
        
        popped = self.head.data
        self.head = self.head.next
        return popped

    def display(self):
        if self.isempty():
            print("List is Empty! nothing to see.")
            return None

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        print(elements)


a = linkedlist(3)
a.insert_front(1)
a.insert_end(3)
a.insert_front(2)
a.insert_front(4)
a.display()
a.delete()
a.display()
a.delete()
a.delete()
a.delete()
a.display()