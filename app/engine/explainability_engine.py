class ExplainabilityEngine:

    # =================================
    # SEARCH EXPLANATIONS
    # =================================

    @staticmethod
    def explain_search(algorithm):

        explanations = {

            "bfs": [

                "BFS expands nodes level-by-level.",

                "FIFO queue guarantees shortest path discovery.",

                "BFS is complete and optimal for equal edge costs."
            ],

            "dfs": [

                "DFS explores deeply before backtracking.",

                "Uses stack-based traversal.",

                "DFS is memory efficient but not always optimal."
            ],

            "greedy": [

                "Greedy search selects nodes using heuristics.",

                "Fast exploration reduces search time.",

                "Optimality is not guaranteed."
            ],

            "astar": [

                "A* combines path cost and heuristic estimate.",

                "Admissible heuristics ensure optimality.",

                "Balances speed and optimality."
            ]
        }

        return explanations.get(
            algorithm,
            []
        )

    # =================================
    # CSP EXPLANATIONS
    # =================================

    @staticmethod
    def explain_csp():

        return [

            "MRV selected the variable with minimum remaining values.",

            "Backtracking explored valid assignments incrementally.",

            "Constraint propagation reduced invalid states.",

            "Forward checking prevented future conflicts.",

            "Conflict-free timetable assignment generated."
        ]

    # =================================
    # MINIMAX EXPLANATIONS
    # =================================

    @staticmethod
    def explain_minimax():

        return [

            "MAX node attempted to maximize utility.",

            "MIN node simulated adversarial responses.",

            "Alpha-Beta pruning removed dominated branches.",

            "Utility score selected optimal policy."
        ]

    # =================================
    # BAYESIAN EXPLANATIONS
    # =================================

    @staticmethod
    def explain_bayes():

        return [

            "Observed evidence updated prior probabilities.",

            "Conditional probabilities adjusted belief state.",

            "Posterior probability estimated scheduling risk.",

            "Inference performed using Bayesian reasoning."
        ]