#include <iostream>
#include <string>

using namespace std ;

#define MAX 5


class Stack
{
    private:
    int values[MAX];
    int top;
    
    public:
    Stack()
    {
        top = -1;
    }

    //to push
    void push(int num)
    {
        if (top == MAX -1)
        {
            cout << "Stack Overflow. \n";
            return;
    
        }
        top++;
        values[top]= num;
        
        cout <<"Pushed" << num << "to stack." << endl ;
    }
    void pop()
    {
        if (top == -1)
        {
            cout<< "Stack Underflow. \n";
            return;
        }
        cout << values[top] << "removed. \n";
        top --;
        
    }
    
    void peek()
    {
        if (top == -1)
        {
            cout << "nothing to see. \n";
            return;
        }
        cout << "top value is:  " << values[top] << endl;
    }
    void display()
    {
        if (top == -1)
        {
            cout << "nothing to see. \n";
            return;
        }
        cout << "Values in Stack: \n";
        for (int i=top; i>=0; i--)
        {
            cout << values[i] << endl;
        }
    }
};

int main()
{
    Stack s;
    int choice;
    int num;
    char ans;
    
    do
    {
        cout << "---- Stack Menu ----" <<endl;
        cout << "1. Push" <<endl;
        cout << "2. Pop" <<endl;
        cout << "3. Peek" <<endl;
        cout << "4. Display" <<endl;
        cout << "Enter your choice :" <<endl;
        cin >> choice;

        switch(choice)
        {
            case 1:
            cout <<"Enter Value:    " << endl;
            cin >> num;
            s.push(num);
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

            default :
            cout <<"Invalid, Try again!" <<endl;

        }
        cout<<"Do you want to continue?(y/n):"<<endl;
        cin>>ans;
    } 
    while (ans == 'Y' || ans == 'y');
    return 0;
    
};