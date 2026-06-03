#include "../include/BST.h"

#include <iostream>

BST::BST()
{
    root = nullptr;
}

BSTNode* BST::insertNode(
    BSTNode* node,
    const std::string& name,
    int value
)
{
    if(node == nullptr)
    {
        return new BSTNode(
            name,
            value
        );
    }

    if(value < node->value)
    {
        node->left =
            insertNode(
                node->left,
                name,
                value
            );
    }
    else
    {
        node->right =
            insertNode(
                node->right,
                name,
                value
            );
    }

    return node;
}

void BST::insert(
    const std::string& name,
    int value
)
{
    root =
        insertNode(
            root,
            name,
            value
        );
}

void BST::inorderNode(
    BSTNode* node
)
{
    if(node == nullptr)
        return;

    inorderNode(node->left);

    std::cout
        << node->name
        << " "
        << node->value
        << std::endl;

    inorderNode(node->right);
}

void BST::inorder()
{
    inorderNode(root);
}