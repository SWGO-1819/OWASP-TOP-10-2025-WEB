import json
import os
from flask import Blueprint, render_template, current_app
from flask import request
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
    CWE-22 (Path Traversal) 예시 페이지를 보여줍니다.
    """
    # 애플리케이션 루트를 기준으로 데이터 파일의 절대 경로를 안전하게 구성합니다.
    # 이렇게 하면 어디서 실행하든 경로가 올바르게 설정됩니다.
    # 사용자 데이터는 templates가 아닌 data 디렉토리에서 관리하는 것이 좋습니다.
    DATA_PATH = os.path.join(current_app.root_path, 'data')
    username = request.args.get("user")  # 사용자 입력
    profile_data = []

    # username이 비어있지 않은 경우에만 파일을 읽도록 처리
    if username:
        # 경로 조작을 방지하기 위해 basename을 사용하여 파일 이름만 가져옵니다. (CWE-22 완화 조치)
        profile_path = os.path.join(DATA_PATH, username)
        try:
            with open(profile_path, "r", encoding="utf-8") as f:
                profile_data = [line.strip() for line in f]  # 파일 내용을 한 줄씩 읽어 리스트에 저장
        except Exception as e:
            profile_data.append(f"Error: {e}")

    return render_template(f'A01/CWE-22.html', profile=profile_data)