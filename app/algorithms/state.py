class TimetableState:

    def __init__(self):
        self.assignments = []
        self.cost = 0
        self.reasoning = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def add_reasoning(self, message):
        self.reasoning.append(message)

    def add_cost(self, value):
        self.cost += value

    def to_dict(self):
        return {
            "assignments": self.assignments,
            "cost": self.cost,
            "reasoning": self.reasoning
        }