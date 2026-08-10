#include <iostream>
#include <string>

using namespace std;

#define MAX 5

class Queue 
{
    private:
    int arr [MAX];
    int front, rear;

    public:
    Queue() {
        front = -1;
        rear = -1;
    }

    //enqueue op.
    void enqueue(int value) 
    {
        if (rear == MAX-1)
        {
            cout << "Queue Overflow." << endl;
            return;
        }
        if (front == -1)
        front = 0;
        rear ++;
        arr[rear] = value;
        cout << value << " Inserted into the queue." <<endl;
    }

    void dequeue()
    {
        if (front == -1 || front > rear)
        {
            cout << "Queue Underflow. queue is empty." << endl;
            return;
        }
        cout << arr[front] << " Delected from Queue." << endl;
        front ++;
        if (front > rear) 
        {
            front = rear = -1;
        }
    }

    void display()
    {
        if (front == -1) 
        {
            cout << "Nothing to display." << endl;
            return;
        }
        cout  << "Queue elements:";
        for (int i = front; i <=rear; i++)
        {
            cout << arr [i] << " ";
        }
        cout << endl;
    }

};

int main() {
    Queue q;
    int choice, value;

    do {
        cout <<"\n ---- Queue operations ----";
        cout <<"\n 1.Enqueue";
        cout <<"\n 2.Dequeue";
        cout <<"\n 3.Display";
        cout <<"\n 4.Exit program";
        cout <<"\n Enter choice:    ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                cout  << "Enter value to insert:    ";
                cin >> value;
                q.enqueue (value);
                break;

            case 2:
                q.dequeue ();
                break;

            case 3:
                q.display();
                break;

            case 4:
                cout << "bye!" << endl;
                break;

            default:
                cout << "Invalid choice! try again :P" << endl;

        }

    } while (choice != 4);
    return 0;
};