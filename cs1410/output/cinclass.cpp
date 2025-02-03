#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedListIterator {
private:
    Node* current;

public:
    LinkedListIterator(Node* node) : current(node) {}

    int operator*() const {
        return current->data;
    }

    LinkedListIterator& operator++() {
        if (current) current = current->next;
        return *this;
    }

    LinkedListIterator operator++(int) {
        LinkedListIterator temp = *this;
        if (current) current = current->next;
        return temp;
    }

    bool operator!=(const LinkedListIterator& other) const {
        return current != other.current;
    }
};

class LinkedList {
private:
    Node* head;
    Node* tail;

public:
    LinkedList() : head(nullptr), tail(nullptr) {}

    void append(int val) {
        Node* newNode = new Node(val);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    LinkedListIterator begin() {
        return LinkedListIterator(head);
    }

    LinkedListIterator end() {
        return LinkedListIterator(nullptr);
    }
};

int main() {
    LinkedList list;
    list.append(10);
    list.append(20);
    list.append(30);
    list.append(40);
    list.append(50);

    cout << "Linked List Elements: ";
    
    for (LinkedListIterator it = list.begin(); it != list.end(); it++) {
        cout << *it << " ";
    }
    
    cout << endl;

    return 0;
}
