class UtilityAgent:

    def utility(self, state):

        score = 100

        conflicts = state.get(
            "conflicts",
            0
        )

        gaps = state.get(
            "faculty_gaps",
            0
        )

        room_changes = state.get(
            "room_changes",
            0
        )

        score -= conflicts * 20
        score -= gaps * 5
        score -= room_changes * 3

        return score

    def choose_best_policy(
        self,
        states
    ):

        best_state = None
        best_score = float("-inf")

        for state in states:

            score = self.utility(state)

            if score > best_score:

                best_score = score
                best_state = state

        return {
            "best_policy": best_state,
            "utility": best_score
        }