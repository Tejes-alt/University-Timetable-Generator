class DFS:

    def search(self, graph, start, goal):

        stack = [
            (start, [start])
        ]

        visited = set()

        while stack:

            node, path = stack.pop()

            if node == goal:
                return path

            if node not in visited:

                visited.add(node)

                for neighbor in graph.get(node, []):

                    stack.append(
                        (
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None