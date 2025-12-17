import json
import os
from flask import Blueprint, render_template, current_app
from flask import request

a10_bp = Blueprint('a10', __name__, url_prefix='/A10')

@a10_bp.route('/')
def a10_index():
    json_path = os.path.join(current_app.root_path, 'data', 'A10.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A10.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A10/A10.html', cwes=cwe_data)