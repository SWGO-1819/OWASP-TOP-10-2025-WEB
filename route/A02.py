import json
import os
from flask import Blueprint, render_template, current_app
from flask import request

a02_bp = Blueprint('a02', __name__, url_prefix='/A02')

@a02_bp.route('/')
def a02_index():
    """
    A01 취약점 테스트 메인 페이지를 보여줍니다.
    templates/A01/A01.html 파일을 렌더링합니다.
    """
    # A01.json 파일 경로 설정
    json_path = os.path.join(current_app.root_path, 'data', 'A02.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A02.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A02/A02.html', cwes=cwe_data)

@a02_bp.route('/cwe-5', methods=['GET', 'POST'])
def cwe_5():
    """
    CWE-22 (Path Traversal) 예시 페이지를 보여줍니다.
    """
    # A01.json 파일에서 CWE 데이터를 읽어옵니다.
    json_path = os.path.join(current_app.root_path, 'data', 'A02.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A01.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A02/CWE-5.html', cwes=cwe_data)