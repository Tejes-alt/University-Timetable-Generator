from app import create_app, db
from app.models import Department, Faculty, Subject, Room, Section, Course, CourseSession, TimeSlot, BlockedTimeSlot, User

def seed_database():
    app = create_app()
    with app.app_context():
        print("Dropping tables...")
        db.drop_all()
        print("Creating tables...")
        db.create_all()
        
        # Add admin
        admin = User(username="admin", role="admin")
        admin.set_password("admin123")
        db.session.add(admin)

        # 1 Department
        dept = Department(name="Computer Science", code="CSE")
        db.session.add(dept)
        db.session.commit()

        # 4 Faculty
        faculties = []
        for i in range(1, 5):
            f = Faculty(name=f"Professor {i}", email=f"prof{i}@cse.edu", department_id=dept.id, max_hours_per_day=4)
            db.session.add(f)
            faculties.append(f)
        db.session.commit()

        # 5 Subjects
        subjects = []
        sub_names = ["Algorithms", "Data Structures", "AI", "Databases", "Networks"]
        for i, name in enumerate(sub_names):
            s = Subject(code=f"CS10{i}", name=name, is_lab=False, department_id=dept.id)
            db.session.add(s)
            subjects.append(s)
        db.session.commit()

        # 3 Rooms
        for i in range(1, 4):
            db.session.add(Room(name=f"Room {i}", capacity=100, is_lab=False))
        db.session.commit()

        # 1 Section
        sec = Section(name="CSE-A Sem 1", semester=1, students_count=60, department_id=dept.id)
        db.session.add(sec)
        db.session.commit()

        # Courses mapping (1 section takes all 5 subjects)
        for i, s in enumerate(subjects):
            fac = faculties[i % len(faculties)]
            c = Course(section_id=sec.id, subject_id=s.id, faculty_id=fac.id, contact_hours=3) # 3 sessions per subject
            db.session.add(c)
            db.session.flush()
            for s_num in range(1, 4):
                sess = CourseSession(course_id=c.id, session_number=s_num)
                db.session.add(sess)
        db.session.commit()
        
        # 5 Periods / Day (Monday to Friday)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        times = [
            ("09:00", "10:00"), ("10:00", "11:00"), 
            ("11:00", "12:00"), ("12:00", "13:00"), ("13:00", "14:00")
        ]
        timeslots = []
        for day in days:
            for start, end in times:
                timeslots.append(TimeSlot(day_of_week=day, start_time=start, end_time=end))
        db.session.add_all(timeslots)
        db.session.commit()
        
        print("Database seeded with Lightweight configuration (15 sessions).")

if __name__ == '__main__':
    seed_database()
