from flask import Blueprint, render_template

from app.models import Timetable

main_bp = Blueprint(
    'main',
    __name__
)

# =====================================
# DASHBOARD
# =====================================

@main_bp.route('/')
def dashboard():

    return render_template(
        'dashboard.html'
    )

# =====================================
# GENERATION VIEW
# =====================================

@main_bp.route('/generate-view')
def generation_view():

    return render_template(
        'generation.html'
    )

# =====================================
# DYNAMIC TIMETABLE
# =====================================

@main_bp.route('/timetable')
def timetable_view():

    timetable_entries = [

        {
            "day": "Monday",
            "time": "09:00",
            "subject": "Algorithms",
            "faculty": "Professor 1",
            "room": "Room 1",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        },

        {
            "day": "Monday",
            "time": "10:00",
            "subject": "Data Structures",
            "faculty": "Professor 2",
            "room": "Room 2",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        },

        {
            "day": "Tuesday",
            "time": "09:00",
            "subject": "Artificial Intelligence",
            "faculty": "Professor 3",
            "room": "Room 1",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        },

        {
            "day": "Tuesday",
            "time": "11:00",
            "subject": "Databases",
            "faculty": "Professor 4",
            "room": "Room 3",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        },

        {
            "day": "Wednesday",
            "time": "09:00",
            "subject": "Computer Networks",
            "faculty": "Professor 1",
            "room": "Room 2",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        },

        {
            "day": "Thursday",
            "time": "10:00",
            "subject": "Algorithms",
            "faculty": "Professor 2",
            "room": "Room 1",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        },

        {
            "day": "Friday",
            "time": "09:00",
            "subject": "Artificial Intelligence",
            "faculty": "Professor 3",
            "room": "Room 3",
            "section": "CSE-A Sem 1",
            "department": "Computer Science",
            "department_code": "CSE",
            "is_lab": False
        }

    ]

    class FakeTimetable:
        name = "AI Generated Timetable"
        status = "Published"
        score = 97

    return render_template(
        "timetable.html",
        timetable=FakeTimetable(),
        timetable_entries=timetable_entries
    )

# =====================================
# AI ALGORITHMS PAGE
# =====================================

@main_bp.route("/algorithms")
def algorithms():

    return render_template(
        "algorithms.html"
    )

# =====================================
# SEARCH LAB
# =====================================

@main_bp.route("/search-lab")
def search_lab():

    return render_template(
        "search_lab.html"
    )

# =====================================
# UNCERTAINTY ENGINE
# =====================================

@main_bp.route("/uncertainty")
def uncertainty():

    return render_template(
        "uncertainty.html"
    )

# =====================================
# DECISION ENGINE
# =====================================

@main_bp.route("/decision-engine")
def decision_engine():

    return render_template(
        "decision_engine.html"
    )

# =====================================
# ANALYTICS DASHBOARD
# =====================================

@main_bp.route("/analytics")
def analytics():

    return render_template(
        "analytics.html"
    )

@main_bp.route("/pipeline")
def pipeline():

    return render_template(
        "pipeline.html"
    )