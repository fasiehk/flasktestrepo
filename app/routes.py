
from flask import request, redirect, jsonify, Blueprint
from . import db
from .models import URL
import string
import random

shortener_bp = Blueprint('shortener', __name__)

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(length))
    return short_url

@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('original_url')
    custom_alias = data.get('custom_alias')

    if custom_alias:
        existing_url = URL.query.filter_by(custom_alias=custom_alias).first()
        if existing_url:
            return jsonify({'error': 'Custom alias already in use'}), 400
        short_url = custom_alias
    else:
        short_url = generate_short_url()
        while URL.query.filter_by(short_url=short_url).first():
            short_url = generate_short_url()

    new_url = URL(original_url=original_url, short_url=short_url, custom_alias=custom_alias)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({'short_url': short_url}), 201

@shortener_bp.route('/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)