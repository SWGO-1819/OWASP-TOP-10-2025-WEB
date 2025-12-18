import os
from flask import Flask, render_template
# from route.sign import sign_bp  # 나중에 필요시 주석 해제하여 사용
# from route.userlist import list_bp
# from route.call import call_bp

# --- 취약점 Blueprint 임포트 ---
from route.A01 import a01_bp
from route.A02 import a02_bp
from route.A03 import a03_bp
from route.A04 import a04_bp
from route.A05 import a05_bp
from route.A06 import a06_bp
from route.A07 import a07_bp
from route.A08 import a08_bp
from route.A09 import a09_bp
from route.A10 import a10_bp

from models import db


# Flask 애플리케이션 생성
app = Flask(__name__)

# 데이터베이스 파일이 저장될 instance 폴더가 존재하는지 확인하고, 없으면 생성합니다.
# 이 코드는 SQLAlchemy 설정 전에 위치해야 합니다.
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# 데이터베이스 경로를 Flask의 공식 instance_path를 사용하도록 수정합니다.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL",
    f"sqlite:///{os.path.join(app.instance_path, 'app.db')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# 애플리케이션의 기본 설정을 할 수 있습니다. (예: 비밀키)
app.secret_key = 'your-very-secret-key'


# OWASP Top 10 목록을 정의합니다.
# 이 데이터는 나중에 별도의 설정 파일로 분리할 수도 있습니다.
OWASP_TOP_10_2025 = [
    {"id": "A01", "name": "Broken Access Control", "url": "/A01"},
    {"id": "A02", "name": "Security Misconfiguration", "url": "/A02"},
    {"id": "A03", "name": "Software Supply Chain Failures", "url": "/A03"},
    {"id": "A04", "name": "Cryptographic Failures", "url": "/A04"},
    {"id": "A05", "name": "Injection", "url": "/A05"},
    {"id": "A06", "name": "Insecure Design", "url": "/A06"},
    {"id": "A07", "name": "Authentication Failures", "url": "/A07"},
    {"id": "A08", "name": "Software or Data Integrity Failures", "url": "/A08"},
    {"id": "A09", "name": "Security Logging and Alerting Failures", "url": "/A09"},
    {"id": "A10", "name": "Mishandling of Exceptional Conditions", "url": "/A10"},
]

@app.route('/')
def index():
    """
    메인 인덱스 페이지를 렌더링합니다.
    OWASP Top 10 각 항목에 대한 링크 목록을 보여줍니다.
    """
    return render_template('index.html', vulnerabilities=OWASP_TOP_10_2025)

# --- Blueprint 등록 ---
# route 폴더에 정의된 Blueprint들을 여기에 등록합니다.
# 예: app.register_blueprint(sign_bp)
# app.register_blueprint(list_bp)
# app.register_blueprint(call_bp)

# 취약점 Blueprint를 애플리케이션에 등록합니다.
app.register_blueprint(a01_bp)
app.register_blueprint(a02_bp)
app.register_blueprint(a03_bp)
app.register_blueprint(a04_bp)
app.register_blueprint(a05_bp)
app.register_blueprint(a06_bp)
app.register_blueprint(a07_bp)
app.register_blueprint(a08_bp)
app.register_blueprint(a09_bp)
app.register_blueprint(a10_bp)


# 애플리케이션 실행
if __name__ == '__main__':
    # debug=True 모드는 개발 중에 유용하며, 코드 변경 시 서버를 자동으로 재시작합니다.
    app.run(debug=True)