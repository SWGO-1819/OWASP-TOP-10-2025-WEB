import json
import os
from flask import Blueprint, render_template, current_app

# 'a01' 블루프린트를 생성합니다. 
# url_prefix='/A01' 설정으로 이 블루프린트 내의 모든 라우트는 '/A01'을 기본 경로로 가집니다.
a01_bp = Blueprint('a01', __name__, url_prefix='/A01')

@a01_bp.route('/')
def a01_index():
    """
    A01 취약점 테스트 메인 페이지를 보여줍니다.
    templates/A01/A01.html 파일을 렌더링합니다.
    """
    # A01.json 파일 경로 설정
    json_path = os.path.join(current_app.root_path, 'data', 'A01.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A01.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A01/A01.html', cwes=cwe_data)

@a01_bp.route('/cwe-22')
def cwe_22():
    """
    CWE-22 (Improper Authorization) 예시 페이지를 보여줍니다.
    """
    return render_template('A01/CWE-22.html')