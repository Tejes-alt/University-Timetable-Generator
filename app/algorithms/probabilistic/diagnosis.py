from app.algorithms.probabilistic.bayesian_network import BayesianNetwork


class DiagnosisSystem:

    def diagnose(
        self,
        faculty_unavailable,
        room_conflict
    ):

        network = BayesianNetwork()

        result = (
            network.infer_failure_probability(
                faculty_unavailable,
                room_conflict
            )
        )

        if (
            result["failure_probability"]
            > 0.7
        ):

            diagnosis = (
                "High scheduling failure risk"
            )

        else:

            diagnosis = (
                "Low scheduling failure risk"
            )

        return {
            "diagnosis": diagnosis,
            "details": result
        }