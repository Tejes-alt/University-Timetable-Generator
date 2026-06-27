class MinimaxAgent:

    def minimax(
        self,
        depth,
        maximizing,
        utility_function
    ):

        if depth == 0:
            return utility_function()

        if maximizing:

            best = float("-inf")

            for _ in range(3):

                value = self.minimax(
                    depth - 1,
                    False,
                    utility_function
                )

                best = max(best, value)

            return best

        else:

            best = float("inf")

            for _ in range(3):

                value = self.minimax(
                    depth - 1,
                    True,
                    utility_function
                )

                best = min(best, value)

            return best