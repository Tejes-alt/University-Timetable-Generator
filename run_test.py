from app import create_app
from app.models import CourseSession, Room, TimeSlot, BlockedTimeSlot
from app.algorithms.csp_solver import CSPSolver
import logging

logging.basicConfig(level=logging.DEBUG)

def test():
    app = create_app()
    with app.app_context():
        course_sessions = CourseSession.query.all()
        rooms = Room.query.all()
        timeslots = TimeSlot.query.all()
        blocked_slots = BlockedTimeSlot.query.all()
        print(f"Loaded {len(course_sessions)} sessions, {len(rooms)} rooms, {len(timeslots)} timeslots")
        
        solver = CSPSolver(course_sessions, rooms, timeslots, blocked_slots, max_faculty_hours=6)
        print("Solver initialized. Starting execution...")
        success = solver.solve()
        print(f"Success: {success}")
        print(f"Nodes expanded: {solver.explainer.stats['nodes_expanded']}")
        print(f"Backtracks: {solver.explainer.stats['backtracks']}")
        
if __name__ == '__main__':
    test()
