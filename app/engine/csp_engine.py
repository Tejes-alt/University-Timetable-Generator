variables = {

    "Math": ["Mon-9", "Tue-10"],

    "Physics": ["Mon-9", "Wed-11"],

    "Chemistry": ["Tue-10", "Thu-12"]
}

constraints = [

    ("Math", "Physics")
]

def solve_csp():

    assignment = {}

    trace = []

    def is_valid(var, value):

        for other_var, other_value in assignment.items():

            if value == other_value:

                trace.append(

                    f"Conflict detected between "
                    f"{var} and {other_var}"

                )

                return False

        return True

    def backtrack():

        if len(assignment) == len(variables):

            trace.append(
                "Complete assignment found"
            )

            return True

        unassigned = [

            v for v in variables
            if v not in assignment
        ]

        var = unassigned[0]

        trace.append(
            f"Selected variable {var}"
        )

        for value in variables[var]:

            trace.append(
                f"Trying {value} for {var}"
            )

            if is_valid(var, value):

                assignment[var] = value

                if backtrack():

                    return True

                del assignment[var]

        return False

    backtrack()

    return {

        "assignment": assignment,

        "trace": trace
    }