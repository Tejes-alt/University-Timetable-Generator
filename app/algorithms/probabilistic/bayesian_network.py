class BayesianNetwork:

    def __init__(self):

        self.network = {
            "FacultyUnavailable": {
                True: 0.2,
                False: 0.8
            },

            "RoomConflict": {
                True: 0.1,
                False: 0.9
            },

            "ScheduleFailure": {
                (True, True): 0.95,
                (True, False): 0.7,
                (False, True): 0.6,
                (False, False): 0.05
            }
        }

    def infer_failure_probability(
        self,
        faculty_unavailable,
        room_conflict
    ):

        probability = (
            self.network["ScheduleFailure"][
                (
                    faculty_unavailable,
                    room_conflict
                )
            ]
        )

        return {
            "failure_probability": probability
        }