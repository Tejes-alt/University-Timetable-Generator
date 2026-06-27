class ConstraintProof:

    @staticmethod
    def prove_constraint(
        constraint_name,
        result,
        details
    ):

        return {
            "constraint": constraint_name,
            "satisfied": result,
            "proof": details
        }