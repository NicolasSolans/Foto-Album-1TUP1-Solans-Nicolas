from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from . import db
from .models import Photo
from .schemas import PhotoCreateSchema
from typing import List, Tuple, Any

photo_bp = Blueprint('photo_bp', __name__)

@photo_bp.route("/")
def index() -> str:
    photos: List[Tuple[Any]] = Photo.query.all()

    return render_template('index.html', photos=photos)

@photo_bp.route("/photos/new")
def new_photo_form() -> str:
    return render_template('photo_form.html')

@photo_bp.route('/photos', methods=['POST'])
def create_photo() -> str:
    data: Tuple[Any] = request.form

    try:
        photo_data = PhotoCreateSchema(title=data['title'],
                                       description=data['description'],
                                       image=str(data['image']))
        
    except ValueError as e:
        return jsonify({"error": e}), 400

    new_photo = Photo(title=data['title'],
                        description=data['description'],
                        image=str(data['image']))
    
    db.session.add(new_photo)
    db.session.commit()

    return render_template('base.html', photo=new_photo)