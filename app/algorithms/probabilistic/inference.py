class InferenceEngine:

    @staticmethod
    def variable_elimination(
        probabilities
    ):

        result = sum(
            probabilities
        ) / len(probabilities)

        return {
            "inference_result": result,
            "method": "Variable Elimination"
        }

    @staticmethod
    def message_passing(
        messages
    ):

        combined = sum(messages)

        return {
            "belief_update": combined,
            "method": "Message Passing"
        }