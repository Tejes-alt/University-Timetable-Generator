class ReasoningTrace:

    def __init__(self):

        self.steps = []

    def add_step(
        self,
        component,
        message
    ):

        self.steps.append({
            "component": component,
            "message": message
        })

    def get_trace(self):

        return self.steps