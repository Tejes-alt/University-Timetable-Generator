import heapq


class AStar:

    def search(
        self,
        graph,
        heuristics,
        start,
        goal
    ):

        pq = []

        heapq.heappush(
            pq,
            (
                heuristics[start],
                0,
                start,
                [start]
            )
        )

        visited = set()

        while pq:

            f_cost, g_cost, node, path = heapq.heappop(pq)

            if node == goal:
                return path, g_cost

            if node not in visited:

                visited.add(node)

                for neighbor, edge_cost in graph.get(node, []):

                    new_cost = g_cost + edge_cost

                    heapq.heappush(
                        pq,
                        (
                            new_cost + heuristics[neighbor],
                            new_cost,
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None