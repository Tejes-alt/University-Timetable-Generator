from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), default='admin')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Department(db.Model):
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)

    faculties = db.relationship('Faculty', backref='department', lazy=True)
    subjects = db.relationship('Subject', backref='department', lazy=True)
    sections = db.relationship('Section', backref='department', lazy=True)

class Faculty(db.Model):
    __tablename__ = 'faculty'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    max_hours_per_day = db.Column(db.Integer, default=6)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    
class BlockedTimeSlot(db.Model):
    __tablename__ = 'blocked_time_slot'
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=True) # if null, it's a global block
    day_of_week = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    reason = db.Column(db.String(100), nullable=True) # e.g. "Lunch Break" or "Meeting"

class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    is_lab = db.Column(db.Boolean, default=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    is_lab = db.Column(db.Boolean, default=False)

class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) # e.g., "A", "B", "CS-A"
    semester = db.Column(db.Integer, nullable=False)
    students_count = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

class Course(db.Model):
    """Mapping of Subject to Section with designated Faculty. Core grouping entity."""
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    contact_hours = db.Column(db.Integer, default=3) # total hours per week
    
    section = db.relationship('Section', backref='courses')
    subject = db.relationship('Subject', backref='courses')
    faculty = db.relationship('Faculty', backref='courses')
    sessions = db.relationship('CourseSession', backref='course', cascade='all, delete-orphan')

class CourseSession(db.Model):
    """Represents a single contact hour occurrence of a Course -> Fixed duplicate session bug"""
    __tablename__ = 'course_session'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    session_number = db.Column(db.Integer, nullable=False) # 1, 2, 3...

class TimeSlot(db.Model):
    __tablename__ = 'time_slot'
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(20), nullable=False) # Monday, Tuesday...
    start_time = db.Column(db.String(10), nullable=False) # 09:00
    end_time = db.Column(db.String(10), nullable=False) # 10:00

class Timetable(db.Model):
    __tablename__ = 'timetable'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Draft') # Draft, Published, etc.
    is_active = db.Column(db.Boolean, default=True)
    score = db.Column(db.Integer, default=0) # For min conflict optimization
    
    entries = db.relationship('TimetableEntry', backref='timetable', cascade='all, delete-orphan')

class TimetableEntry(db.Model):
    __tablename__ = 'timetable_entry'
    id = db.Column(db.Integer, primary_key=True)
    timetable_id = db.Column(db.Integer, db.ForeignKey('timetable.id'), nullable=False)
    course_session_id = db.Column(db.Integer, db.ForeignKey('course_session.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    timeslot_id = db.Column(db.Integer, db.ForeignKey('time_slot.id'), nullable=False)
    
    course_session = db.relationship('CourseSession', backref='timetable_entries')
    room = db.relationship('Room', backref='timetable_entries')
    timeslot = db.relationship('TimeSlot', backref='timetable_entries')
