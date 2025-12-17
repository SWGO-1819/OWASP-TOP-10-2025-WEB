import json
import os
from flask import Blueprint, render_template, current_app
from flask import request

a08_bp = Blueprint('a08', __name__, url_prefix='/A08')

@a08_bp.route('/')
def a08_index():
    json_path = os.path.join(current_app.root_path, 'data', 'A08.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A08.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A08/A08.html', cwes=cwe_data)