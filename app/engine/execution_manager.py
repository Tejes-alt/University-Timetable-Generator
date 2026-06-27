from app.engine.explainability_engine import (
    ExplainabilityEngine
)

from app.engine.search_engine import (
    bfs,
    dfs,
    greedy
)

from app.engine.csp_engine import (
    solve_csp
)

from app.engine.decision_engine import (
    minimax
)

from app.engine.uncertainty_engine import (
    bayesian_inference
)

from app.engine.explainability_engine import (
    ExplainabilityEngine
)

class ExecutionManager:

    # =================================
    # SEARCH
    # =================================

    @staticmethod
    def run_search(algorithm):

        if algorithm == "bfs":

            trace = bfs()

        elif algorithm == "dfs":

            trace = dfs()

        elif algorithm == "greedy":

            trace = greedy()

        else:

            trace = []

        explanations = (
            ExplainabilityEngine
            .explain_search(algorithm)
        )

        return {

            "trace": trace,

            "explanations": explanations
        }

    # =================================
    # CSP
    # =================================

    @staticmethod
    def run_csp():

        result = solve_csp()

        result["explanations"] = (

            ExplainabilityEngine
            .explain_csp()

        )

        return result

    # =================================
    # DECISION
    # =================================

    @staticmethod
    def run_decision():

        result = minimax()

        result["explanations"] = (

            ExplainabilityEngine
            .explain_minimax()

        )

        return result

    # =================================
    # UNCERTAINTY
    # =================================

    @staticmethod
    def run_uncertainty():

        result = bayesian_inference()

        result["explanations"] = (

            ExplainabilityEngine
            .explain_bayes()

        )

        return result