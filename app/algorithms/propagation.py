class Propagation:

    @staticmethod
    def forward_checking(
        assignments,
        variable,
        value,
        domains,
        constraints
    ):

        new_domains = {
            var: list(vals)
            for var, vals in domains.items()
        }

        for neighbor in constraints.get(variable, []):

            if value in new_domains[neighbor]:

                new_domains[neighbor].remove(value)

                if not new_domains[neighbor]:
                    return None

        return new_domains