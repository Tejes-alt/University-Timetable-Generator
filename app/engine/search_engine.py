from collections import deque
import heapq

graph = {

    "A": ["B", "C"],

    "B": ["D", "E"],

    "C": ["F"],

    "D": [],

    "E": ["G"],

    "F": [],

    "G": []
}

heuristics = {

    "A": 7,
    "B": 4,
    "C": 3,
    "D": 6,
    "E": 2,
    "F": 1,
    "G": 0
}

# =====================================
# BFS
# =====================================

def bfs(start="A", goal="G"):

    visited = set()

    queue = deque([start])

    trace = []

    while queue:

        node = queue.popleft()

        trace.append(
            f"Expanded node {node}"
        )

        if node == goal:

            trace.append(
                "Goal reached"
            )

            return trace

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                queue.append(neighbor)

    return trace

# =====================================
# DFS
# =====================================

def dfs(start="A", goal="G"):

    visited = set()

    stack = [start]

    trace = []

    while stack:

        node = stack.pop()

        trace.append(
            f"Visited node {node}"
        )

        if node == goal:

            trace.append(
                "Goal reached"
            )

            return trace

        if node not in visited:

            visited.add(node)

            for neighbor in reversed(
                graph[node]
            ):

                stack.append(neighbor)

    return trace

# =====================================
# GREEDY
# =====================================

def greedy(start="A", goal="G"):

    pq = []

    heapq.heappush(
        pq,
        (
            heuristics[start],
            start
        )
    )

    visited = set()

    trace = []

    while pq:

        _, node = heapq.heappop(pq)

        trace.append(
            f"Heuristic selected {node}"
        )

        if node == goal:

            trace.append(
                "Goal reached"
            )

            return trace

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                heapq.heappush(
                    pq,
                    (
                        heuristics[neighbor],
                        neighbor
                    )
                )

    return trace