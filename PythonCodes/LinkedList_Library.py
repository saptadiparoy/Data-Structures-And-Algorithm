#using singly linked list for library management system

class Book:
    #initialising the node
    def __init__ (self, bid):
        self.bid = bid
        self.next = None #pointer to next


class Library:
    def __init__(self):
        self.head = None

    def Book_in_end(self, bid):
        new_book = Book(bid)
        if not self.head:
            self.head = new_book
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_book

    def Book_at_start(self, bid):
        new_book = Book(bid)
        new_book.next = self.head
        self.head = new_book

    def delete_book (self):
        if self.head is None:
            print ("Empty")
            return None

        top= self.head
        self.head = self.head.next
        return top.bid
    
    def display(self):
        elements = []

        current = self.head
        while current:
            elements.append(str(current.bid))
            current = current.next

        print (elements)

lib = Library()

if __name__ == "__main__":
    while True:
        print ("----LIBRARY----")
        print ("1. Insert book at start \n2. Insert book at end \n3. Delete a book \n4. Display Library \n5. Exit")
        choice = int(input("Enter your choice:  "))

        if choice == 1:
            bookid = (input("Enter bookid:   "))
            lib.Book_at_start(bookid)
            print (f"Book:{bookid} added to start of library list.")

        elif choice == 2:
            bookid = (input("Enter Bookid:   "))
            lib.Book_in_end(bookid)
            print (f"Book:{bookid} added to end of library list.")

        elif choice == 3:
            lib.delete_book()
            print (f"Book deleted!")

        elif choice == 4:
            lib.display()

        elif choice == 5:
            print ("Bye!")
            break

        else:
            print ("Invalid choice, try again!")
