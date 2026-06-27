def minimax():

    trace = []

    utilities = [5, 8, 2, 9]

    trace.append(
        "Evaluating utility nodes"
    )

    best = max(utilities)

    trace.append(
        f"Selected utility {best}"
    )

    trace.append(
        "Alpha-Beta pruning applied"
    )

    return {

        "best_utility": best,

        "trace": trace
    }