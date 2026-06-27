import heapq


class GreedySearch:

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
                start,
                [start]
            )
        )

        visited = set()

        while pq:

            _, node, path = heapq.heappop(pq)

            if node == goal:
                return path

            if node not in visited:

                visited.add(node)

                for neighbor in graph.get(node, []):

                    heapq.heappush(
                        pq,
                        (
                            heuristics[neighbor],
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None