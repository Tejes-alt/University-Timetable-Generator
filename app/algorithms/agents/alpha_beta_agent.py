class AlphaBetaAgent:

    def alpha_beta(
        self,
        depth,
        alpha,
        beta,
        maximizing,
        utility_function
    ):

        if depth == 0:
            return utility_function()

        if maximizing:

            value = float("-inf")

            for _ in range(3):

                value = max(
                    value,
                    self.alpha_beta(
                        depth - 1,
                        alpha,
                        beta,
                        False,
                        utility_function
                    )
                )

                alpha = max(alpha, value)

                if beta <= alpha:
                    break

            return value

        else:

            value = float("inf")

            for _ in range(3):

                value = min(
                    value,
                    self.alpha_beta(
                        depth - 1,
                        alpha,
                        beta,
                        True,
                        utility_function
                    )
                )

                beta = min(beta, value)

                if beta <= alpha:
                    break

            return value