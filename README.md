# 🚀 Asteroid Miner

A 2D resource management game built with a hybrid Python + C++ architecture, developed as an academic project at **Universidad Distrital Francisco José de Caldas**.

---

## 📖 Overview

Asteroid Miner is a 2D game where players control a mining unit that must collect resources from asteroids while managing limited fuel. The game integrates multiple algorithmic paradigms — greedy selection, backtracking optimization, and efficient data structures — within an interactive real-time environment.

---

## 👨‍💻 Authors

| Name | Role | Email |
|------|------|-------|
| Luis Alejandro Morales | Systems Engineering Student | lamoralesn@udistrital.edu.co |
| Juan Manuel Otálora Hernández | Systems Engineering Student | jmotalorah@udistrital.edu.co |
| Julian Felipe Donoso | Systems Engineering Student | jfdonosoh@udistrital.edu.co |

---

## 🎮 Game Description

The player starts from a fixed base and must navigate a 2D space to mine asteroids, each with a position `(x, y)` and a resource value. The core constraint is fuel: movement consumes fuel proportional to the Euclidean distance traveled, and the player must return safely to base.

Each level features a unique asteroid distribution and fuel budget, with increasing difficulty across levels. Performance is evaluated at the end of each level:

| Stars | Condition |
|-------|-----------|
| ⭐⭐⭐ | Result equals the optimal solution |
| ⭐⭐ | At least 75% of the optimal value collected |
| ⭐ | Minimum resource threshold met |
| ❌ | Failed to return to base or below minimum threshold |

---

## 🏗️ Architecture

The system uses a **hybrid architecture** combining two languages:

- **Python** — Game logic, algorithm execution, and visualization via [Pygame](https://www.pygame.org/).
- **C++** — Efficient data structure management (route history lists and asteroid BST catalog).

Communication between components is handled through **JSON files**, ensuring a clean separation of concerns and facilitating modularity, scalability, and testing.

```
┌─────────────────────────┐        JSON        ┌──────────────────────────┐
│      Python Module       │ ◄────────────────► │       C++ Module          │
│  - Game logic            │                    │  - Route history (List)   │
│  - Algorithm execution   │                    │  - Asteroid catalog (BST) │
│  - Pygame visualization  │                    │                           │
└─────────────────────────┘                    └──────────────────────────┘
```

---

## ⚙️ Algorithms

### 1. Greedy Asteroid Selection

Prioritizes asteroids by their **value-to-distance ratio**, providing fast, real-time decisions.

```
For each asteroid aᵢ:
    rᵢ = valueᵢ / distance(current_position, aᵢ)

Sort asteroids by rᵢ in descending order → return sorted list
```

- ✅ Very fast (near-instantaneous)
- ⚠️ Does not always guarantee the maximum total value

### 2. Optimal Route via Backtracking

Exhaustively explores all feasible routes under the fuel constraint to guarantee the **optimal solution**.

```
Explore(route, remaining_fuel, value):
    if value > best_value:
        best_value = value
        best_route = route
    for each asteroid aᵢ not in route:
        cost = distance(current_position, aᵢ)
        if remaining_fuel - cost ≥ 0:
            Explore(route ∪ {aᵢ}, remaining_fuel - cost, value + vᵢ)
```

- ✅ Guarantees the globally optimal route
- ⚠️ Higher computational cost as asteroid count grows; used as a benchmark

---

## 🗂️ Data Structures (C++)

| Structure | Purpose |
|-----------|---------|
| **Linked List** | Stores the history of visited asteroids for efficient traversal and route reconstruction |
| **Binary Search Tree (BST)** | Maintains an ordered catalog of asteroids by value, supporting efficient insertion, search, and retrieval |

---

## 🛠️ Tech Stack

- **Python** — Game logic and visualization
- **Pygame** — 2D rendering, user input, real-time state updates
- **C++** — Data structure management
- **JSON** — Inter-module communication

---

## 📦 Installation

### Prerequisites

- Python 3.x
- Pygame
- A C++ compiler (g++ / clang++)

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/asteroid-miner.git
cd asteroid-miner

# Install Python dependencies
pip install pygame

# Compile the C++ module
g++ -o asteroid_structures src/cpp/structures.cpp

# Run the game
python src/main.py
```
