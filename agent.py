import timeit
import statistics
from collections import deque

# ============================================================
# SLE-2: EMPIRICAL PERFORMANCE ANALYSIS
# BFS VS DFS ON THE SAME GRID
# ============================================================

ROWS = 20
COLS = 20

START = (0, 0)
GOAL = (19, 19)

# 0 = Free cell
# 1 = Blocked cell
GRID = [
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "01111111111111111110",
    "00000000000000000000",
    "00000000000000000000"
]


def valid_neighbors(node):
    r, c = node

    moves = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    )

    for dr, dc in moves:
        nr = r + dr
        nc = c + dc

        if (
            0 <= nr < ROWS
            and 0 <= nc < COLS
            and GRID[nr][nc] == "0"
        ):
            yield (nr, nc)


# ============================================================
# BREADTH-FIRST SEARCH
# ============================================================

def bfs_search():
    queue = deque([START])

    visited = {START}
    parent = {START: None}

    expanded = 0

    while queue:

        current = queue.popleft()
        expanded += 1

        if current == GOAL:
            break

        for neighbor in valid_neighbors(current):

            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if GOAL not in parent:
        return None, expanded

    path_length = 0
    node = GOAL

    while parent[node] is not None:
        path_length += 1
        node = parent[node]

    return path_length, expanded


# ============================================================
# DEPTH-FIRST SEARCH
# ============================================================

def dfs_search():

    stack = [START]

    visited = {START}
    parent = {START: None}

    expanded = 0

    while stack:

        current = stack.pop()
        expanded += 1

        if current == GOAL:
            break

        neighbors = list(valid_neighbors(current))

        for neighbor in reversed(neighbors):

            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    if GOAL not in parent:
        return None, expanded

    path_length = 0
    node = GOAL

    while parent[node] is not None:
        path_length += 1
        node = parent[node]

    return path_length, expanded


# ============================================================
# PERFORMANCE PROFILING
# ============================================================

def run_profiling():

    print("\n" + "=" * 60)
    print("       SLE-2 EMPIRICAL PERFORMANCE ANALYSIS")
    print("=" * 60)

    print("Problem      : 20 x 20 Grid Search")
    print("Start        :", START)
    print("Goal         :", GOAL)
    print("Algorithms   : BFS vs DFS")

    # Correctness check
    bfs_path, bfs_nodes = bfs_search()
    dfs_path, dfs_nodes = dfs_search()

    print("\nCORRECTNESS CHECK")
    print("-" * 60)

    print(
        "BFS -> Path length:",
        bfs_path,
        "| Nodes expanded:",
        bfs_nodes
    )

    print(
        "DFS -> Path length:",
        dfs_path,
        "| Nodes expanded:",
        dfs_nodes
    )

    if bfs_path is None or dfs_path is None:
        print("No solution found.")
        return

    # Profiling settings
    runs = 5
    iterations = 5000

    bfs_times = []
    dfs_times = []

    print("\nPROFILING")
    print("5 runs, 5000 iterations per run")
    print("-" * 60)

    for run in range(1, runs + 1):

        bfs_total = timeit.timeit(
            bfs_search,
            number=iterations
        )

        dfs_total = timeit.timeit(
            dfs_search,
            number=iterations
        )

        bfs_times.append(bfs_total)
        dfs_times.append(dfs_total)

        print(
            f"Run {run}: "
            f"BFS = {bfs_total:.6f}s, "
            f"DFS = {dfs_total:.6f}s"
        )

    # Average execution time
    avg_bfs_total = statistics.mean(bfs_times)
    avg_dfs_total = statistics.mean(dfs_times)

    bfs_ms = (avg_bfs_total / iterations) * 1000
    dfs_ms = (avg_dfs_total / iterations) * 1000

    print("\n" + "=" * 60)
    print("FINAL RESULTS")
    print("=" * 60)

    print(
        f"Average BFS time/execution : "
        f"{bfs_ms:.6f} ms"
    )

    print(
        f"Average DFS time/execution : "
        f"{dfs_ms:.6f} ms"
    )

    print("BFS nodes expanded         :", bfs_nodes)
    print("DFS nodes expanded         :", dfs_nodes)

    print("BFS path length            :", bfs_path)
    print("DFS path length            :", dfs_path)

    print("\nTHEORY CONNECTION")
    print("-" * 60)

    print(
        "BFS explores nodes level by level and "
        "finds the shortest path in an unweighted grid."
    )

    print(
        "DFS explores nodes deeply first and "
        "does not guarantee the shortest path."
    )

    print(
        "Execution time can vary depending on "
        "the computer and Python runtime."
    )

    print("\nSLE-2 profiling completed successfully.")


# ============================================================
# MAIN
# ============================================================

def main():

    while True:

        print("\n" + "=" * 45)
        print("          SLE-2 PERFORMANCE ANALYSIS")
        print("=" * 45)

        print("1. Run BFS vs DFS Profiling")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            run_profiling()

        elif choice == "2":
            print("\nSLE-2 program terminated.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
