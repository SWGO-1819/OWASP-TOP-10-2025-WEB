import json
import os
from flask import Blueprint, render_template, current_app
from flask import request

# 'a04' 블루프린트를 생성합니다.
# url_prefix='/A04' 설정으로 이 블루프린트 내의 모든 라우트는 '/A04'를 기본 경로로 가집니다.
a04_bp = Blueprint('a04', __name__, url_prefix='/A04')

@a04_bp.route('/')
def a04_index():
    """
    A04 취약점 테스트 메인 페이지를 보여줍니다.
    templates/A04/A04.html 파일을 렌더링합니다.
    """
    # A04.json 파일 경로 설정
    json_path = os.path.join(current_app.root_path, 'data', 'A04.json')
    cwe_data = []
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            cwe_data = json.load(f)
    except FileNotFoundError:
        current_app.logger.error(f"A04.json not found at {json_path}")
    except json.JSONDecodeError:
        current_app.logger.error(f"Error decoding JSON from {json_path}")

    return render_template('A04/A04.html', cwes=cwe_data)