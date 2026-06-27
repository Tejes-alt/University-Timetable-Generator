from app.algorithms.probabilistic.markov_model import MarkovModel


class TrackingSystem:

    def track_schedule_state(
        self,
        current_state
    ):

        model = MarkovModel()

        probabilities = (
            model.next_state_probability(
                current_state
            )
        )

        predicted_state = max(
            probabilities,
            key=probabilities.get
        )

        return {
            "current_state": current_state,
            "predicted_next_state":
                predicted_state,
            "transition_probabilities":
                probabilities
        }