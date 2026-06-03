#include "../include/LinkedList.h"
#include <fstream>
#include <iostream>
#include <fstream>

LinkedList::LinkedList()
{
    head = nullptr;
}

void LinkedList::insert(
    const std::string& route
)
{
    Node* newNode =
        new Node(route);

    if(head == nullptr)
    {
        head = newNode;
        return;
    }

    Node* current = head;

    while(current->next != nullptr)
    {
        current = current->next;
    }

    current->next = newNode;
}

void LinkedList::print()
{
    Node* current = head;

    while(current != nullptr)
    {
        std::cout
            << current->route
            << std::endl;

        current = current->next;
    }
}

LinkedList::~LinkedList()
{
    Node* current = head;

    while(current != nullptr)
    {
        Node* temp = current;

        current = current->next;

        delete temp;
    }
}

void LinkedList::saveToFile(
    const std::string& filename
)
{
    std::ofstream file(
        filename,
        std::ios::app
    );

    Node* current = head;

    while(current)
    {
        file
            << current->route
            << std::endl;

        current = current->next;
    }

    file.close();
}

void LinkedList::appendToFile(
    const std::string& filename
)
{
    std::ofstream file(
        filename,
        std::ios::app
    );

    Node* current = head;

    while(current != nullptr)
    {
        file
            << current->route
            << std::endl;

        current = current->next;
    }

    file.close();
}