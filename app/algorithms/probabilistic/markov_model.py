class MarkovModel:

    def __init__(self):

        self.transition_matrix = {

            "Stable": {
                "Stable": 0.8,
                "Conflict": 0.2
            },

            "Conflict": {
                "Stable": 0.4,
                "Conflict": 0.6
            }
        }

    def next_state_probability(
        self,
        current_state
    ):

        return self.transition_matrix[
            current_state
        ]