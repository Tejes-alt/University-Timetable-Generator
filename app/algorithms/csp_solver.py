from app.algorithms.state import TimetableState
from app.algorithms.constraints import Constraints
from app.algorithms.heuristics import Heuristics
from app.algorithms.propagation import Propagation
from app.algorithms.optimization import Optimization
from app.algorithms.explainability import Explainability


class CSPSolver:

    def __init__(self):

        self.rooms = [
            "Room-101",
            "Room-102",
            "Lab-1"
        ]

        self.timeslots = [
            "9AM",
            "10AM",
            "11AM",
            "1PM",
            "2PM"
        ]

    def is_valid(
        self,
        assignments,
        assignment
    ):

        if Constraints.faculty_conflict(
            assignments,
            assignment["faculty"],
            assignment["timeslot"]
        ):
            return False

        if Constraints.room_conflict(
            assignments,
            assignment["room"],
            assignment["timeslot"]
        ):
            return False

        if Constraints.section_conflict(
            assignments,
            assignment["section"],
            assignment["timeslot"]
        ):
            return False

        return True

    def backtrack(
        self,
        subjects,
        index,
        state
    ):

        if index >= len(subjects):
            return True

        subject = subjects[index]

        domain = []

        for room in self.rooms:
            for timeslot in self.timeslots:

                domain.append({
                    "room": room,
                    "timeslot": timeslot
                })

        domain = Heuristics.least_constraining_value(
            domain,
            lambda value: 0
        )

        for value in domain:

            assignment = {
                "subject": subject["subject"],
                "faculty": subject["faculty"],
                "section": subject["section"],
                "room": value["room"],
                "timeslot": value["timeslot"]
            }

            if self.is_valid(
                state.assignments,
                assignment
            ):

                state.add_assignment(
                    assignment
                )

                Explainability.success(
                    state,
                    assignment
                )

                result = self.backtrack(
                    subjects,
                    index + 1,
                    state
                )

                if result:
                    return True

                state.assignments.pop()

                state.add_reasoning(
                    f"Backtracked from "
                    f"{assignment['subject']}"
                )

            else:

                Explainability.rejection(
                    state,
                    f"Constraint violation for "
                    f"{assignment['subject']}"
                )

        return False

    def solve(self, subjects):

        state = TimetableState()

        self.backtrack(
            subjects,
            0,
            state
        )

        evaluation = (
            Optimization.evaluate_solution(
                state.assignments
            )
        )

        return {
            "assignments": state.assignments,
            "reasoning": state.reasoning,
            "evaluation": evaluation
        }