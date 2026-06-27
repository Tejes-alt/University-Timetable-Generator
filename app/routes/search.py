from flask import Blueprint, jsonify, request
from app.models import Department, Faculty, Subject, Room, Section
from sqlalchemy import or_

search_bp = Blueprint('search', __name__)

@search_bp.route('/', methods=['GET'])
def search_all():
    query = request.args.get('q', '').lower()
    
    faculties = []
    rooms = []
    subjects = []
    departments = []
    sections = []
    
    if query:
        # Faculty search
        f_res = Faculty.query.filter(Faculty.name.ilike(f"%{query}%")).limit(5).all()
        faculties = [{'id': f.id, 'name': f.name, 'type': 'Faculty'} for f in f_res]
        
        # Room search
        r_res = Room.query.filter(Room.name.ilike(f"%{query}%")).limit(5).all()
        rooms = [{'id': r.id, 'name': r.name, 'type': 'Room'} for r in r_res]
        
        # Subject search
        s_res = Subject.query.filter(or_(Subject.name.ilike(f"%{query}%"), Subject.code.ilike(f"%{query}%"))).limit(5).all()
        subjects = [{'id': s.id, 'name': s.name, 'type': 'Subject'} for s in s_res]
        
        # Department search
        d_res = Department.query.filter(or_(Department.name.ilike(f"%{query}%"), Department.code.ilike(f"%{query}%"))).limit(5).all()
        departments = [{'id': d.id, 'name': d.name, 'type': 'Department'} for d in d_res]
        
        # Section search
        sec_res = Section.query.filter(Section.name.ilike(f"%{query}%")).limit(5).all()
        sections = [{'id': s.id, 'name': s.name, 'type': 'Section'} for s in sec_res]
        
    return jsonify({
        'suggestions': faculties + rooms + subjects + departments + sections
    })

@search_bp.route('/filters', methods=['GET'])
def get_filters():
    # Return all filter options dynamically
    depts = [{'id': d.id, 'name': d.name} for d in Department.query.all()]
    facs = [{'id': f.id, 'name': f.name} for f in Faculty.query.all()]
    rms = [{'id': r.id, 'name': r.name} for r in Room.query.all()]
    return jsonify({
        'departments': depts,
        'faculties': facs,
        'rooms': rms
    })
