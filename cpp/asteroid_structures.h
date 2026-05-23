// Simple asteroid structures, BST and linked list, and algorithm declarations
#ifndef ASTEROID_STRUCTURES_H
#define ASTEROID_STRUCTURES_H

#include <vector>
#include <string>

struct Asteroid
{
   int id;
   double x;
   double y;
   double value;
};

// Simple singly-linked list to store a route (sequence of asteroid ids)
class RouteList
{
public:
   struct Node
   {
      int asteroid_id;
      Node *next;
      Node(int id) : asteroid_id(id), next(nullptr) {}
   };

   RouteList();
   ~RouteList();
   void push_back(int asteroid_id);
   void clear();
   std::vector<int> to_vector() const;

private:
   Node *head;
   Node *tail;
};

// Binary Search Tree keyed by asteroid value (descending order insertion is supported)
class AsteroidBST
{
public:
   AsteroidBST();
   ~AsteroidBST();
   void insert(const Asteroid &a);
   std::vector<Asteroid> inorder() const; // ascending by value

private:
   struct Node
   {
      Asteroid a;
      Node *left;
      Node *right;
      Node(const Asteroid &ast) : a(ast), left(nullptr), right(nullptr) {}
   };
   Node *root;
   void destroy(Node *n);
   void insert_node(Node *&n, const Asteroid &a);
   void inorder_node(Node *n, std::vector<Asteroid> &out) const;
};

// Algorithms
// Greedy selection by value/distance ratio. Returns pair(route ids, total value)
std::pair<std::vector<int>, double> greedy_select(
    const std::vector<Asteroid> &asteroids,
    double start_x, double start_y,
    double base_x, double base_y,
    double fuel_budget);

// Backtracking optimal route. Exhaustive search that returns best route and value.
std::pair<std::vector<int>, double> backtracking_optimal(
    const std::vector<Asteroid> &asteroids,
    double start_x, double start_y,
    double base_x, double base_y,
    double fuel_budget);

#endif // ASTEROID_STRUCTURES_H
