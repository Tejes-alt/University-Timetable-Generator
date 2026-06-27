class ExplainableOutput:

    @staticmethod
    def build(
        schedule,
        reasoning,
        constraints,
        inference
    ):

        return {
            "schedule": schedule,
            "reasoning_trace": reasoning,
            "constraint_proofs": constraints,
            "inference_steps": inference
        }