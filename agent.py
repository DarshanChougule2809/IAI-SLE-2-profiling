import random
import timeit
import statistics
from collections import deque

# ============================================================
# SLE-1: STUDY ASSISTANT AI AGENT
# SLE-2: EMPIRICAL PERFORMANCE ANALYSIS
# ============================================================

def greet_user():
    return "Hello! I am your Study Assistant. How can I help you?"


def calculate_percentage():
    marks = []
    print("\nEnter marks of 5 subjects (0-100):")

    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / 5

    print("Total Marks:", total)
    print("Percentage:", f"{percentage:.2f}%")

    if percentage >= 75:
        print("Result: Excellent performance!")
    elif percentage >= 60:
        print("Result: Very good performance!")
    elif percentage >= 40:
        print("Result: You passed. Keep improving!")
    else:
        print("Result: Need more practice.")


def get_study_tip():
    tips = [
        "Study for 25 minutes and take a 5-minute break.",
        "Make short notes while studying.",
        "Practice previous question papers.",
        "Revise difficult topics regularly.",
        "Keep your phone away while studying."
    ]
    return random.choice(tips)


def simple_calculator():
    print("\nSimple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")


# ============================================================
# SLE-2: SEARCH PROBLEM
# BFS VS DFS ON THE SAME GRID
# ============================================================

ROWS = 20
COLS = 20
START = (0, 0)
GOAL = (19, 19)

# Fixed grid: the same problem is used for BFS and DFS.
# 0 = free cell, 1 = blocked cell.
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
    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < ROWS
            and 0 <= nc < COLS
            and GRID[nr][nc] == "0"
        ):
            yield (nr, nc)


def bfs_search():
    """Breadth-First Search. Returns path length and nodes expanded."""
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


def dfs_search():
    """Depth-First Search. Returns path length and nodes expanded."""
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

        # Reverse order makes the traversal deterministic.
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


def run_profiling():
    print("\n" + "=" * 60)
    print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
    print("=" * 60)
    print("Problem : 20 x 20 grid search")
    print("Start   :", START)
    print("Goal    :", GOAL)
    print("Algorithms: BFS vs DFS")

    # Correctness check before profiling.
    bfs_path, bfs_nodes = bfs_search()
    dfs_path, dfs_nodes = dfs_search()

    print("\nCorrectness check")
    print("BFS -> Path length:", bfs_path, "| Nodes expanded:", bfs_nodes)
    print("DFS -> Path length:", dfs_path, "| Nodes expanded:", dfs_nodes)

    if bfs_path is None or dfs_path is None:
        print("No solution found.")
        return

    # The benchmark repeats the same deterministic search many times.
    # This makes the measured time stable enough to compare.
    runs = 5
    iterations = 5000

    bfs_times = []
    dfs_times = []

    print("\nProfiling: 5 runs, 5000 iterations per run")

    for run in range(1, runs + 1):
        bfs_total = timeit.timeit(bfs_search, number=iterations)
        dfs_total = timeit.timeit(dfs_search, number=iterations)

        bfs_times.append(bfs_total)
        dfs_times.append(dfs_total)

        print(
            f"Run {run}: "
            f"BFS total = {bfs_total:.6f}s, "
            f"DFS total = {dfs_total:.6f}s"
        )

    avg_bfs_total = statistics.mean(bfs_times)
    avg_dfs_total = statistics.mean(dfs_times)

    bfs_ms = (avg_bfs_total / iterations) * 1000
    dfs_ms = (avg_dfs_total / iterations) * 1000

    print("\n" + "-" * 60)
    print("FINAL RESULTS")
    print("-" * 60)
    print(f"Average BFS time/execution : {bfs_ms:.6f} ms")
    print(f"Average DFS time/execution : {dfs_ms:.6f} ms")
    print(f"BFS nodes expanded         : {bfs_nodes}")
    print(f"DFS nodes expanded         : {dfs_nodes}")
    print(f"BFS path length             : {bfs_path}")
    print(f"DFS path length             : {dfs_path}")

    if bfs_ms < dfs_ms:
        print("Time observation: BFS was faster in this run.")
    elif dfs_ms < bfs_ms:
        print("Time observation: DFS was faster in this run.")
    else:
        print("Time observation: Both were nearly equal in this run.")

    if bfs_nodes < dfs_nodes:
        print("Node observation: BFS expanded fewer nodes.")
    elif dfs_nodes < bfs_nodes:
        print("Node observation: DFS expanded fewer nodes.")
    else:
        print("Node observation: Both expanded the same number of nodes.")

    print("\nTheory connection:")
    print("- BFS explores nodes level by level and finds a shortest path")
    print("  in an unweighted grid.")
    print("- DFS explores deeply first and does not guarantee a shortest path.")
    print("- Actual timing depends on the computer and Python runtime.")

    print("\nSLE-2 profiling completed successfully.")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    print(greet_user())

    while True:
        print("\n" + "=" * 45)
        print("             STUDY ASSISTANT")
        print("=" * 45)
        print("1. Calculate Percentage")
        print("2. Get Study Tip")
        print("3. Use Calculator")
        print("4. Run SLE-2 BFS vs DFS Profiling")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            calculate_percentage()
        elif choice == "2":
            print("\nStudy Tip:", get_study_tip())
        elif choice == "3":
            simple_calculator()
        elif choice == "4":
            run_profiling()
        elif choice == "5":
            print("\nGoodbye! Keep studying!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
