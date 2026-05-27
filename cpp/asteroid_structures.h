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
struct RouteListNode
{
   int asteroid_id;
   RouteListNode *next;
};

struct RouteList
{
   RouteListNode *head;
   RouteListNode *tail;
};

void routelist_init(RouteList &list);
void routelist_clear(RouteList &list);
void routelist_push_back(RouteList &list, int asteroid_id);
std::vector<int> routelist_to_vector(const RouteList &list);

// Binary Search Tree keyed by asteroid value
struct AsteroidBSTNode
{
   Asteroid a;
   AsteroidBSTNode *left;
   AsteroidBSTNode *right;
};

struct AsteroidBST
{
   AsteroidBSTNode *root;
};

void bst_init(AsteroidBST &bst);
void bst_clear(AsteroidBST &bst);
void bst_insert(AsteroidBST &bst, const Asteroid &a);
std::vector<Asteroid> bst_inorder(const AsteroidBST &bst); // ascending by value

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
