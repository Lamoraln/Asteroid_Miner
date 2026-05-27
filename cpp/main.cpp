#include <iostream>
#include "asteroid_structures.h"
#include <vector>

int main()
{
   // sample asteroids (id, x, y, value)
   std::vector<Asteroid> asteroids = {
       {1, 2.0, 3.0, 10.0},
       {2, -1.0, 4.0, 12.0},
       {3, 5.0, -2.0, 8.0},
       {4, 3.0, 3.0, 15.0},
       {5, -2.0, -1.0, 7.0},
       {6, 4.5, 1.0, 9.0}};

   double start_x = 0.0, start_y = 0.0;
   double base_x = 0.0, base_y = 0.0;
   double fuel = 10.0; // example fuel budget

   std::cout << "Running greedy selection (fuel=" << fuel << ")\n";
   auto greedy = greedy_select(asteroids, start_x, start_y, base_x, base_y, fuel);
   std::cout << "Greedy route ids:";
   for (int id : greedy.first)
      std::cout << ' ' << id;
   std::cout << " | total value=" << greedy.second << "\n\n";

   std::cout << "Running backtracking optimal (fuel=" << fuel << ")\n";
   auto opt = backtracking_optimal(asteroids, start_x, start_y, base_x, base_y, fuel);
   std::cout << "Optimal route ids:";
   for (int id : opt.first)
      std::cout << ' ' << id;
   std::cout << " | total value=" << opt.second << "\n";

   // Demonstrate BST usage
   AsteroidBST bst;
   bst_init(bst);
   for (auto &a : asteroids)
      bst_insert(bst, a);
   auto sorted = bst_inorder(bst);
   bst_clear(bst);
   std::cout << "\nAsteroids inorder by value (ascending):\n";
   for (auto &a : sorted)
   {
      std::cout << "id=" << a.id << " value=" << a.value << " pos=(" << a.x << "," << a.y << ")\n";
   }

   return 0;
}
