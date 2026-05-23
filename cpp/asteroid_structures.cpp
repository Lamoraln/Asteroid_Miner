#include "asteroid_structures.h"
#include <cmath>
#include <limits>
#include <iostream>
#include <algorithm>
#include <functional>

// --- RouteList implementation ---
RouteList::RouteList() : head(nullptr), tail(nullptr) {}

RouteList::~RouteList() { clear(); }

void RouteList::push_back(int asteroid_id)
{
   Node *n = new Node(asteroid_id);
   if (!head)
      head = tail = n;
   else
   {
      tail->next = n;
      tail = n;
   }
}

void RouteList::clear()
{
   Node *cur = head;
   while (cur)
   {
      Node *tmp = cur->next;
      delete cur;
      cur = tmp;
   }
   head = tail = nullptr;
}

std::vector<int> RouteList::to_vector() const
{
   std::vector<int> out;
   Node *cur = head;
   while (cur)
   {
      out.push_back(cur->asteroid_id);
      cur = cur->next;
   }
   return out;
}

// --- AsteroidBST implementation ---
AsteroidBST::AsteroidBST() : root(nullptr) {}

AsteroidBST::~AsteroidBST() { destroy(root); }

void AsteroidBST::destroy(Node *n)
{
   if (!n)
      return;
   destroy(n->left);
   destroy(n->right);
   delete n;
}

void AsteroidBST::insert(const Asteroid &a) { insert_node(root, a); }

void AsteroidBST::insert_node(Node *&n, const Asteroid &a)
{
   if (!n)
   {
      n = new Node(a);
      return;
   }
   if (a.value < n->a.value)
      insert_node(n->left, a);
   else
      insert_node(n->right, a);
}

void AsteroidBST::inorder_node(Node *n, std::vector<Asteroid> &out) const
{
   if (!n)
      return;
   inorder_node(n->left, out);
   out.push_back(n->a);
   inorder_node(n->right, out);
}

std::vector<Asteroid> AsteroidBST::inorder() const
{
   std::vector<Asteroid> out;
   inorder_node(root, out);
   return out;
}

// --- Helper functions ---
static double dist(double x1, double y1, double x2, double y2)
{
   double dx = x1 - x2;
   double dy = y1 - y2;
   return std::sqrt(dx * dx + dy * dy);
}

// --- Greedy algorithm ---
std::pair<std::vector<int>, double> greedy_select(
    const std::vector<Asteroid> &asteroids,
    double start_x, double start_y,
    double base_x, double base_y,
    double fuel_budget)
{
   std::vector<bool> used(asteroids.size(), false);
   double cx = start_x, cy = start_y;
   double remaining = fuel_budget;
   double total_value = 0.0;
   std::vector<int> route;

   while (true)
   {
      int best_i = -1;
      double best_score = -1.0;
      for (size_t i = 0; i < asteroids.size(); ++i)
      {
         if (used[i])
            continue;
         double d = dist(cx, cy, asteroids[i].x, asteroids[i].y);
         double back = dist(asteroids[i].x, asteroids[i].y, base_x, base_y);
         // ensure we can reach asteroid and then still return to base (conservative)
         if (d + back > remaining)
            continue;
         double score = asteroids[i].value / (d + 1e-9);
         if (score > best_score)
         {
            best_score = score;
            best_i = (int)i;
         }
      }
      if (best_i == -1)
         break;
      // move to best
      double travel = dist(cx, cy, asteroids[best_i].x, asteroids[best_i].y);
      remaining -= travel;
      total_value += asteroids[best_i].value;
      route.push_back(asteroids[best_i].id);
      used[best_i] = true;
      cx = asteroids[best_i].x;
      cy = asteroids[best_i].y;
      // if cannot return to base, undo last and break
      double need_back = dist(cx, cy, base_x, base_y);
      if (need_back > remaining)
      {
         // undo
         remaining += travel;
         total_value -= asteroids[best_i].value;
         route.pop_back();
         break;
      }
   }
   // optionally return to base (not tracked here other than fuel feasibility)
   return {route, total_value};
}

// --- Backtracking optimal route ---
std::pair<std::vector<int>, double> backtracking_optimal(
   const std::vector<Asteroid> &asteroids,
   double start_x, double start_y,
   double base_x, double base_y,
   double fuel_budget
) {
   size_t n = asteroids.size();
   std::vector<bool> used(n, false);
   std::vector<int> cur_route;
   std::vector<int> best_route;
   double best_value = 0.0;

   std::function<void(double, double, double, double)> dfs =
       [&](double cx, double cy, double remaining, double value_so_far)
   {
      // update best by considering returning to base now
      double return_cost = dist(cx, cy, base_x, base_y);
      if (return_cost <= remaining)
      {
         if (value_so_far > best_value)
         {
            best_value = value_so_far;
            best_route = cur_route;
         }
      }
      // try every unused asteroid
      for (size_t i = 0; i < n; ++i)
      {
         if (used[i])
            continue;
         double d = dist(cx, cy, asteroids[i].x, asteroids[i].y);
         // must be able to go there; also need at least enough left to return from there
         double back = dist(asteroids[i].x, asteroids[i].y, base_x, base_y);
         if (d > remaining)
            continue;
         if (d + back > remaining)
            continue;
         used[i] = true;
         cur_route.push_back(asteroids[i].id);
         dfs(asteroids[i].x, asteroids[i].y, remaining - d, value_so_far + asteroids[i].value);
         cur_route.pop_back();
         used[i] = false;
      }
   };

   dfs(start_x, start_y, fuel_budget, 0.0);
   return {best_route, best_value};
}
