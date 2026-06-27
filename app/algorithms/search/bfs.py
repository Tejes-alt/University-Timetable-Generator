from collections import deque


class BFS:

    def search(self, graph, start, goal):

        visited = set()

        queue = deque([
            (start, [start])
        ])

        while queue:

            node, path = queue.popleft()

            if node == goal:
                return path

            if node not in visited:

                visited.add(node)

                for neighbor in graph.get(node, []):

                    queue.append(
                        (
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None