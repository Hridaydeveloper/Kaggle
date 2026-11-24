
#include <iostream>
using namespace std;

// Create a Node
struct Node {
    int data;
    Node* next;
};

Node* head = NULL;

// Insert a node at the end
void insert(int value) {
    Node* newNode = new Node();

    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL) {
        head = newNode;
    }
    else {
        Node* temp = head;

        while (temp->next != NULL) {
            temp = temp->next;
        }

        temp->next = newNode;
    }

    cout << "Node inserted!" << endl;
}

// Display the linked list
void display() {
    Node* temp = head;

    if (head == NULL) {
        cout << "List is empty!" << endl;
        return;
    }

    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }

    cout << "NULL" << endl;
}

// Delete a node by value
void deleteNode(int value) {
    if (head == NULL) {
        cout << "List is empty!" << endl;
        return;
    }

    Node* temp = head;
    Node* prev = NULL;

    // If first node contains the value
    if (head->data == value) {
        head = head->next;
        delete temp;
        cout << "Node deleted!" << endl;
        return;
    }

    // Search for the value
    while (temp != NULL && temp->data != value) {
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) {
        cout << "Value not found!" << endl;
        return;
    }

    prev->next = temp->next;
    delete temp;

    cout << "Node deleted!" << endl;
}

// Reverse the linked list
void reverseList() {
    Node* prev = NULL;
    Node* current = head;
    Node* nextNode = NULL;

    while (current != NULL) {
        nextNode = current->next;
        current->next = prev;
        prev = current;
        current = nextNode;
    }

    head = prev;

    cout << "List reversed!" << endl;
}

// Main function
int main() {
    int choice, value;

    do {
        cout << "\n--- LINKED LIST MENU ---" << endl;
        cout << "1. Insert" << endl;
        cout << "2. Display" << endl;
        cout << "3. Delete" << endl;
        cout << "4. Reverse" << endl;
        cout << "5. Exit" << endl;

        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value: ";
                cin >> value;
                insert(value);
                break;

            case 2:
                display();
                break;

            case 3:
                cout << "Enter value to delete: ";
                cin >> value;
                deleteNode(value);
                break;

            case 4:
                reverseList();
                break;

            case 5:
                cout << "Program ended!" << endl;
                break;

            default:
                cout << "Invalid choice!" << endl;
        }

    } while (choice != 5);

    // Free remaining nodes
    while (head != NULL) {
        Node* temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}
