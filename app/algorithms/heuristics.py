class Heuristics:

    @staticmethod
    def minimum_remaining_values(domains):

        return min(
            domains,
            key=lambda variable: len(domains[variable])
        )

    @staticmethod
    def degree_heuristic(
        variable,
        constraints_graph
    ):

        return len(
            constraints_graph.get(variable, [])
        )

    @staticmethod
    def least_constraining_value(
        values,
        constraints_function
    ):

        return sorted(
            values,
            key=lambda value: constraints_function(value)
        )