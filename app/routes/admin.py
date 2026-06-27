from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)

from app import db

from app.models import (
    Department,
    Faculty,
    Room,
    Subject
)

admin_bp = Blueprint(
    "admin",
    __name__
)

# =====================================
# DASHBOARD
# =====================================

@admin_bp.route("/manage")
def manage_dashboard():

    return render_template(
        "manage_dashboard.html"
    )

# =====================================
# DEPARTMENTS
# =====================================

@admin_bp.route("/manage/departments")
def manage_departments():

    departments = Department.query.all()

    return render_template(

        "manage_departments.html",

        departments=departments
    )

@admin_bp.route(
    "/add-department",
    methods=["POST"]
)
def add_department():

    dept = Department(

        name=request.form["name"],

        code=request.form["code"]
    )

    db.session.add(dept)

    db.session.commit()

    return redirect(
        url_for(
            "admin.manage_departments"
        )
    )

# =====================================
# FACULTY
# =====================================

@admin_bp.route("/manage/faculty")
def manage_faculty():

    faculty = Faculty.query.all()

    return render_template(

        "manage_faculty.html",

        faculty=faculty
    )

@admin_bp.route(
    "/add-faculty",
    methods=["POST"]
)
def add_faculty():

    fac = Faculty(

        name=request.form["name"]
    )

    db.session.add(fac)

    db.session.commit()

    return redirect(
        url_for(
            "admin.manage_faculty"
        )
    )

# =====================================
# ROOMS
# =====================================

@admin_bp.route("/manage/rooms")
def manage_rooms():

    rooms = Room.query.all()

    return render_template(

        "manage_rooms.html",

        rooms=rooms
    )

@admin_bp.route(
    "/add-room",
    methods=["POST"]
)
def add_room():

    room = Room(

        name=request.form["name"],

        capacity=request.form["capacity"]
    )

    db.session.add(room)

    db.session.commit()

    return redirect(
        url_for(
            "admin.manage_rooms"
        )
    )

# =====================================
# SUBJECTS
# =====================================

@admin_bp.route("/manage/subjects")
def manage_subjects():

    subjects = Subject.query.all()

    return render_template(

        "manage_subjects.html",

        subjects=subjects
    )

@admin_bp.route(
    "/add-subject",
    methods=["POST"]
)
def add_subject():

    subject = Subject(

        name=request.form["name"],

        is_lab=
            True if request.form.get("is_lab")
            else False
    )

    db.session.add(subject)

    db.session.commit()

    return redirect(
        url_for(
            "admin.manage_subjects"
        )
    )