#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <string>

struct Node
{
    std::string route;

    Node* next;

    Node(const std::string& r)
    {
        route = r;
        next = nullptr;
    }
};

class LinkedList
{
private:

    Node* head;

public:

    LinkedList();

    void insert(const std::string& route);

    void print();
    
    void saveToFile(const std::string& filename);

    void appendToFile(const std::string& filename);

    ~LinkedList();
};

#endif