class SearchNode:

    def __init__(
        self,
        state,
        parent=None,
        action=None,
        cost=0,
        heuristic=0
    ):

        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    @property
    def total_cost(self):
        return self.cost + self.heuristic