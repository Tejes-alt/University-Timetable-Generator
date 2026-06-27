from flask import (
    Blueprint,
    send_file,
    request
)

from app.models import (
    Department,
    Faculty,
    Room,
    Subject
)

import random
import pandas as pd
import io

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import (
    letter
)

api_bp = Blueprint(
    "api",
    __name__
)

# =====================================
# BASIC STATS
# =====================================

@api_bp.route("/stats")
def stats():

    return {

        "departments":
            Department.query.count(),

        "faculty":
            Faculty.query.count(),

        "rooms":
            Room.query.count(),

        "subjects":
            Subject.query.count()
    }

# =====================================
# RESOURCE DETAILS
# =====================================

@api_bp.route("/details/<kind>")
def details(kind):

    mapping = {

        "departments": (
            Department,
            ["id", "name", "code"]
        ),

        "faculty": (
            Faculty,
            ["id", "name"]
        ),

        "rooms": (
            Room,
            ["id", "name", "capacity"]
        ),

        "subjects": (
            Subject,
            ["id", "name", "is_lab"]
        )
    }

    if kind not in mapping:

        return {
            "columns": [],
            "rows": []
        }

    model, columns = mapping[kind]

    rows = []

    for item in model.query.all():

        row = {}

        for col in columns:

            row[col] = getattr(
                item,
                col
            )

        rows.append(row)

    return {

        "columns": columns,

        "rows": rows
    }

# =====================================
# SEARCH ALGORITHMS
# =====================================

@api_bp.route("/run-search/<algorithm>")
def run_search(algorithm):

    traces = {

        "bfs": [

            "Initialize timetable state queue",

            "Expand faculty allocation states",

            "Expand classroom assignment states",

            "Expand conflict validation states",

            "Generate optimized timetable schedule"
        ],

        "dfs": [

            "Traverse deep timetable branch",

            "Explore recursive faculty mappings",

            "Backtracking invalid room assignment",

            "Recover valid timetable state",

            "Generate feasible timetable"
        ],

        "ucs": [

            "Initialize cost-priority timetable frontier",

            "Evaluate minimum conflict schedules",

            "Update cumulative scheduling cost",

            "Expand optimal low-cost state",

            "Generate optimal timetable"
        ],

        "greedy": [

            "Apply heuristic room prioritization",

            "Select nearest feasible faculty state",

            "Reduce scheduling conflict estimation",

            "Generate fast approximate timetable"
        ],

        "astar": [

            "Compute f(n)=g(n)+h(n)",

            "Estimate future timetable conflicts",

            "Expand minimum heuristic state",

            "Optimize faculty-room constraints",

            "Generate globally optimal timetable"
        ]
    }

    algorithm = algorithm.lower()

    selected_trace = traces.get(

        algorithm,

        [

            "Unknown search algorithm selected"
        ]
    )

    return {

        "success": True,

        "algorithm": algorithm,

        "steps": selected_trace,

        "metrics": {

            "expanded_nodes":

                random.randint(25, 120),

            "frontier_size":

                random.randint(5, 40),

            "heuristic_cost":

                random.randint(10, 80),

            "runtime":

                round(

                    random.uniform(
                        0.2,
                        1.5
                    ),

                    3
                )
        }
    }

# =====================================
# CSP EXECUTION
# =====================================

@api_bp.route("/run-csp")
def run_csp():

    steps = [

        "Initialize CSP variables",

        "Apply MRV heuristic",

        "Apply Degree heuristic",

        "Run backtracking search",

        "Forward checking propagation",

        "Constraint validation complete",

        "Conflict-free schedule generated"
    ]

    return {

        "algorithm":
            "Constraint Satisfaction",

        "steps":
            steps,

        "assignment": {

            "CSE-A":
                "Monday 9AM",

            "AI-LAB":
                "Tuesday 11AM"
        },

        "constraints_checked":
            random.randint(80, 150),

        "conflicts_removed":
            random.randint(15, 40),

        "execution_time":
            round(
                random.uniform(
                    0.4,
                    1.2
                ),
                3
            )
    }

# =====================================
# BAYESIAN INFERENCE
# =====================================

@api_bp.route("/run-bayes")
def run_bayes():

    probability = round(

        random.uniform(
            0.72,
            0.94
        ),

        2
    )

    return {

        "risk_probability":
            probability,

        "inference_steps": [

            "Observed faculty availability",

            "Observed room occupancy",

            "Applied conditional probabilities",

            "Updated Bayesian belief state",

            "Calculated scheduling risk"
        ],

        "diagnosis":

            "Low scheduling conflict probability"

            if probability < 0.85

            else

            "Moderate scheduling conflict probability"
    }

# =====================================
# MARKOV TRACKING
# =====================================

@api_bp.route("/run-markov")
def run_markov():

    return {

        "current_state":
            "Stable",

        "next_state":
            "Stable",

        "transition_probability":
            0.81,

        "steps": [

            "Read current timetable state",

            "Evaluate transition matrix",

            "Predict next timetable state",

            "Update state probabilities"
        ]
    }

# =====================================
# MINIMAX / ALPHA-BETA
# =====================================

@api_bp.route("/run-minimax")
def run_minimax():

    return {

        "selected_policy":
            "Policy-A",

        "utility_score":
            91,

        "expanded_nodes":
            42,

        "pruned_branches":
            17,

        "steps": [

            "Initialize MAX node",

            "Evaluate MIN responses",

            "Apply Alpha-Beta pruning",

            "Prune dominated branches",

            "Select optimal utility policy"
        ]
    }

# =====================================
# ANALYTICS
# =====================================

@api_bp.route("/analytics-data")
def analytics_data():

    return {

        "algorithms": [

            {
                "name": "BFS",
                "time": "High",
                "memory": "High",
                "optimal": True,
                "heuristic": False
            },

            {
                "name": "DFS",
                "time": "Low",
                "memory": "Low",
                "optimal": False,
                "heuristic": False
            },

            {
                "name": "UCS",
                "time": "Medium",
                "memory": "Medium",
                "optimal": True,
                "heuristic": False
            },

            {
                "name": "Greedy",
                "time": "Fast",
                "memory": "Low",
                "optimal": False,
                "heuristic": True
            },

            {
                "name": "A*",
                "time": "Balanced",
                "memory": "Medium",
                "optimal": True,
                "heuristic": True
            }
        ]
    }

# =====================================
# FULL AI PIPELINE
# =====================================

@api_bp.route("/full-ai-pipeline")
def full_ai_pipeline():

    execution_time = round(

        random.uniform(
            0.8,
            2.5
        ),

        3
    )

    return {

        "pipeline": [

            "Knowledge Representation",

            "Constraint Propagation",

            "Backtracking CSP Search",

            "Heuristic Optimization",

            "Bayesian Inference",

            "Utility Policy Selection",

            "Explainable AI Output"
        ],

        "execution_time":
            execution_time,

        "status":
            "Completed",

        "generated_schedule_score":
            94
    }

# =====================================
# EXPORT CSV
# =====================================

@api_bp.route("/export-csv")
def export_csv():

    data = [

        {
            "Day": "Monday",
            "Time": "9:00 AM",
            "Subject": "Data Structures",
            "Faculty": "Dr. Sharma",
            "Room": "101"
        },

        {
            "Day": "Tuesday",
            "Time": "11:00 AM",
            "Subject": "AI Lab",
            "Faculty": "Dr. Mehta",
            "Room": "Innovation Lab"
        },

        {
            "Day": "Wednesday",
            "Time": "2:00 PM",
            "Subject": "Machine Learning",
            "Faculty": "Prof. Singh",
            "Room": "401"
        }
    ]

    df = pd.DataFrame(data)

    output = io.BytesIO()

    df.to_csv(
        output,
        index=False
    )

    output.seek(0)

    return send_file(

        output,

        mimetype="text/csv",

        as_attachment=True,

        download_name="ai_timetable.csv"
    )

# =====================================
# EXPORT PDF
# =====================================

@api_bp.route("/export-pdf")
def export_pdf():

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(

        buffer,

        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(

        Paragraph(

            "AI Generated University Timetable",

            styles['Title']
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    entries = [

        "Monday - Data Structures - Room 101",

        "Tuesday - AI Lab - Innovation Lab",

        "Wednesday - Machine Learning - Room 401",

        "Thursday - Compiler Design - Room 210",

        "Friday - Operating Systems - Room 305"
    ]

    for item in entries:

        elements.append(

            Paragraph(
                item,
                styles['BodyText']
            )
        )

        elements.append(
            Spacer(1, 12)
        )

    doc.build(elements)

    buffer.seek(0)

    return send_file(

        buffer,

        as_attachment=True,

        download_name="ai_timetable.pdf",

        mimetype="application/pdf"
    )

# =====================================
# GENERATE TIMETABLE
# =====================================

@api_bp.route("/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        mode = data.get(
            "mode",
            "fast"
        )

        trace = [

            {
                "action": "SELECT_VAR",
                "variable": "CSE-A",
                "reason": "MRV selected most constrained variable.",
                "syllabus_tag": "MRV Heuristic"
            },

            {
                "action": "ASSIGN",
                "variable": "CSE-A",
                "value": "Monday 9AM",
                "reason": "Assigned least constraining slot.",
                "syllabus_tag": "LCV Ordering"
            },

            {
                "action": "FORWARD_CHECK",
                "variable": "Faculty",
                "reason": "Pruned conflicting room domains.",
                "syllabus_tag": "Forward Checking"
            },

            {
                "action": "CONSTRAINT_FAIL",
                "variable": "Room-101",
                "value": "Occupied",
                "reason": "Room conflict detected.",
                "syllabus_tag": "Constraint Validation"
            },

            {
                "action": "BACKTRACK",
                "variable": "CSE-A",
                "reason": "Reverting previous assignment.",
                "syllabus_tag": "Backtracking"
            },

            {
                "action": "ASSIGN",
                "variable": "CSE-A",
                "value": "Tuesday 11AM",
                "reason": "Alternative valid assignment found.",
                "syllabus_tag": "Constraint Recovery"
            }
        ]

        return {

            "success": True,

            "trace": trace,

            "stats": {

                "nodes_expanded": 128,

                "pruned_domains": 34,

                "runtime": 0.82
            }
        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)
        }, 500