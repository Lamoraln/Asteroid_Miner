#ifndef BST_H
#define BST_H

#include <string>

struct BSTNode
{
    std::string name;
    int value;

    BSTNode* left;
    BSTNode* right;

    BSTNode(const std::string& n, int v)
    {
        name = n;
        value = v;
        left = nullptr;
        right = nullptr;
    }
};

class BST
{
private:

    BSTNode* root;

    BSTNode* insertNode(
        BSTNode* node,
        const std::string& name,
        int value
    );

    void inorderNode(
        BSTNode* node
    );

public:

    BST();

    void insert(
        const std::string& name,
        int value
    );

    void inorder();
};

#endif