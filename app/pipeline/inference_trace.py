class InferenceTrace:

    @staticmethod
    def explain_inference(
        method,
        inputs,
        output
    ):

        return {
            "method": method,
            "inputs": inputs,
            "output": output
        }