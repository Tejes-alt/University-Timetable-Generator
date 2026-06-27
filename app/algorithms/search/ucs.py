import heapq


class UCS:

    def search(self, graph, start, goal):

        pq = []

        heapq.heappush(
            pq,
            (0, start, [start])
        )

        visited = set()

        while pq:

            cost, node, path = heapq.heappop(pq)

            if node == goal:
                return path, cost

            if node not in visited:

                visited.add(node)

                for neighbor, edge_cost in graph.get(node, []):

                    heapq.heappush(
                        pq,
                        (
                            cost + edge_cost,
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None