from flask import request, redirect, jsonify, Blueprint, render_template
from . import db
from .models import URL
import string
import random

shortener_bp = Blueprint('shortener', __name__)

def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@shortener_bp.route('/')
def index():
    return render_template('index.html')

@shortener_bp.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    original_url = data.get('original_url')
    custom_alias = data.get('custom_alias')

    if not original_url:
        return jsonify({'error': 'Original URL is required'}), 400

    if custom_alias:
        if not custom_alias.isalnum():
            return jsonify({'error': 'Custom alias must be alphanumeric'}), 400
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
    url = URL.query.filter_by(short_url=short_url).first()
    if not url:
        return render_template('404.html'), 404  # Render a 404 page if not found
    return redirect(url.original_url)