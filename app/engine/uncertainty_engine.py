import random

def bayesian_inference():

    probability = round(
        random.uniform(
            0.7,
            0.95
        ),
        2
    )

    trace = [

        "Observed faculty availability",

        "Observed room occupancy",

        "Updated conditional probability",

        "Computed posterior belief"
    ]

    return {

        "probability": probability,

        "trace": trace
    }