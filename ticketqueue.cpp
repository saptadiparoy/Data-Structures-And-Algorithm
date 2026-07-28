#include <iostream>
using namespace std;

#define MAX 5

class Queue {
private:
    int arr [MAX];
    int front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;

    }
    //enqueue operation
    void enqueue (int value) {
        if (rear == MAX -1) {
            cout  <<"Queue overflow! cannot insert" << value << endl;
            return;
        }
        if (front == -1)
            front = 0;
        rear ++;
        arr [rear] = value;
        cout << value << "Inserted into the queue." << endl;

    }
    //dequeue operation
    void dequeue () {
        if (front == -1 || front > rear) {
            cout << "Queue Underflow! queue is empty." << endl;
            return;

        }
        cout << arr[front] << "Deleted from queue." << endl;
        front ++;
        if (front > rear) {
            front = rear = -1;

        }
    }

    //display operation
    void display() {
        if (front == -1) {
             cout << "queue is empty." << endl;

        }
        cout <<"Queue Elements:";
        for (int i = front; i <=rear; i++) {
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