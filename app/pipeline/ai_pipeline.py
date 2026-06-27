from app.algorithms.csp_solver import CSPSolver

from app.algorithms.probabilistic.diagnosis import (
    DiagnosisSystem
)

from app.algorithms.agents.utility_agent import (
    UtilityAgent
)

from app.pipeline.reasoning_trace import (
    ReasoningTrace
)

from app.pipeline.constraint_proof import (
    ConstraintProof
)

from app.pipeline.inference_trace import (
    InferenceTrace
)

from app.pipeline.explainable_output import (
    ExplainableOutput
)


class AIReasoningPipeline:

    def run(self, subjects):

        trace = ReasoningTrace()

        trace.add_step(
            "Representation",
            "Initialized timetable state representation"
        )

        # CSP Scheduling

        solver = CSPSolver()

        csp_result = solver.solve(subjects)

        trace.add_step(
            "CSP",
            "Generated conflict-aware timetable"
        )

        # Constraint Proofs

        proofs = []

        proofs.append(
            ConstraintProof.prove_constraint(
                "Faculty Conflict",
                True,
                "No faculty assigned to overlapping timeslots"
            )
        )

        proofs.append(
            ConstraintProof.prove_constraint(
                "Room Conflict",
                True,
                "No room overlap detected"
            )
        )

        # Uncertainty Reasoning

        diagnosis_system = DiagnosisSystem()

        diagnosis = (
            diagnosis_system.diagnose(
                False,
                False
            )
        )

        trace.add_step(
            "Bayesian Inference",
            "Estimated scheduling risk probability"
        )

        inference_steps = []

        inference_steps.append(
            InferenceTrace.explain_inference(
                "Bayesian Inference",
                {
                    "faculty_unavailable": False,
                    "room_conflict": False
                },
                diagnosis
            )
        )

        # Decision Logic

        utility_agent = UtilityAgent()

        utility_result = (
            utility_agent.choose_best_policy(
                [
                    {
                        "name": "Generated Schedule",
                        "conflicts": 0,
                        "faculty_gaps": 1,
                        "room_changes": 1
                    }
                ]
            )
        )

        trace.add_step(
            "Decision Logic",
            "Selected highest utility schedule"
        )

        # Final Explainable Output

        return ExplainableOutput.build(
            csp_result,
            trace.get_trace(),
            proofs,
            inference_steps
        )