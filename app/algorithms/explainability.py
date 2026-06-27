class Explainability:

    @staticmethod
    def success(state, assignment):

        state.add_reasoning(
            f"Assigned {assignment['subject']} "
            f"to {assignment['faculty']} "
            f"in {assignment['room']} "
            f"at {assignment['timeslot']}"
        )

    @staticmethod
    def rejection(state, reason):

        state.add_reasoning(
            f"Rejected Assignment: {reason}"
        )