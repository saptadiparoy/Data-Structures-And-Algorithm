#include <iostream>
#include <string>

using namespace std;

#define MAX 5

class Stack
{
    private:
    string books[MAX];
    int top;

    public:
    Stack()
    {
        top = -1;
    }
    //return book (push)
    void push (string book)
    {
        if (top == MAX -1)
        {
            cout <<"Stack overflow! \n" ;
            return;
        }

        top++;
        books[top] = book;

        cout <<book<<"Inserted into stack. \n";

    }
    void pop()
    {
        if (top == -1)
        {
            cout <<"Stack underflow! \n";
            return;

        }
        cout << books[top] << "Arranged on to the shelf. \n";
        top --;

    }
    void peek()
    {
        if (top == -1)
        {
            cout <<"No books in stack. \n";
            return;
        }
        cout <<"Top Book:" << books[top] << endl;

    }
    void display()
    {
        if (top == -1)
        {
            cout <<"Stack is empty. \n";
            return;
        }

        cout<<"\nBooks (Top to Bottom):\n";

        for(int i=top;i>=0;i--)
        {
            cout<<books[i]<<endl;
        }
    }  
};

int main()
{
    Stack s;
    int choice;
    string book;
    char ans;

    do
    {

        cout<<"------Library Menu------"<<endl;
        cout<<"1.push"<<endl;
        cout<<"2.pop"<<endl;
        cout<<"3.peek"<<endl;
        cout<<"4.display"<<endl;
        cout<<"Enter your choice:"<<endl;
        cin>>choice;

        switch(choice)
        {
            case 1:
            cout<<"Enter book name:"<<endl;
            cin>>book;
            s.push(book);
            break;

            case 2:
            s.pop();
            break;

            case 3:
            s.peek();
            break;

            case 4:
            s.display();
            break;

            default:
            cout<<"Invalid choice"<<endl;
        }
        cout<<"Do you want to continue?(y/n):"<<endl;
        cin>>ans;

    }
    while(ans == 'Y' || ans == 'y');

    return 0;
}