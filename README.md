# IAI-SLE-2-profiling
# SLE-2: Empirical Performance Analysis

## Project Title

**Performance Comparison of BFS and DFS**

## Objective

The objective of SLE-2 is to experimentally compare the performance of **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** using the same 20 × 20 grid problem.

## Algorithms Used

### BFS

Breadth-First Search explores the grid level by level. In an unweighted grid, it can find the shortest path.

### DFS

Depth-First Search explores one path deeply before backtracking. It does not guarantee the shortest path.

## Performance Parameters

The program compares:

* Path length
* Number of nodes expanded
* Execution time
* Average execution time

## Tools Used

* Python 3
* `collections.deque`
* `timeit`
* `statistics`

## Profiling Method

The same fixed grid, start point, and goal point are used for both algorithms.

Each algorithm is executed:

* **5 runs**
* **5000 iterations per run**

The average execution time is calculated using `statistics.mean()`.

## How to Run

Open the project folder in VS Code or Command Prompt and run:

```bash
python agent.py
```

Select:

```text
1. Run BFS vs DFS Profiling
```

## Expected Output

The program displays:

* BFS path length
* DFS path length
* BFS nodes expanded
* DFS nodes expanded
* BFS execution time
* DFS execution time
* Final performance information

## Conclusion

SLE-2 demonstrates how empirical testing can be used to compare two search algorithms. BFS and DFS are tested on exactly the same problem, and their execution time and search behaviour are recorded.
