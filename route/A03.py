import json
import os
from flask import Blueprint, render_template, current_app
from flask import request

# 'a03' 블루프린트를 생성합니다.
# url_prefix='/A03' 설정으로 이 블루프린트 내의 모든 라우트는 '/A03'을 기본 경로로 가집니다.
a03_bp = Blueprint('a03', __name__, url_prefix='/A03')

@a03_bp.route('/')
def a03_index():
    """
    A03 취약점 테스트 메인 페이지를 보여줍니다.
    templates/A03/A03.html 파일을 렌더링합니다.
    """
    # A03.json 파일 경로 설정
    json_path = os.path.join(current_app.root_path, 'data', 'A03.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A03.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A03/A03.html', cwes=cwe_data)