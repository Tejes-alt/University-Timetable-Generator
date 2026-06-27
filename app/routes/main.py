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

    latest_tt = Timetable.query.order_by(
        Timetable.id.desc()
    ).first()

    timetable_entries = []

    if latest_tt:

        for entry in latest_tt.entries:

            course = (
                entry
                .course_session
                .course
            )

            timetable_entries.append({

                "day":
                    entry.timeslot.day_of_week,

                "time":
                    str(
                        entry.timeslot.start_time
                    ),

                "subject":
                    course.subject.name,

                "faculty":
                    course.faculty.name,

                "room":
                    entry.room.name,

                "section":
                    course.section.name,

                "department":
                    course.section.department.name,

                "department_code":
                    course.section.department.code,

                "is_lab":
                    course.subject.is_lab
            })

    return render_template(

        'timetable.html',

        timetable=latest_tt,

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