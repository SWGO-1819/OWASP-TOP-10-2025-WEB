import os
from app import app
from models import db, User, Product

def init_db(reset: bool = True) -> None:
    """
    실습용 DB 초기화.
    reset=True 이면 테이블 전부 삭제 후 재생성(drop_all -> create_all).
    """
    with app.app_context():
        if reset:
            db.drop_all()

        db.create_all()

        # --- seed: users ---
        if not User.query.filter_by(username="admin").first():
            db.session.add(User(username="admin", password="admin123", role="admin"))

        if not User.query.filter_by(username="user").first():
            db.session.add(User(username="user", password="user123", role="user"))

        # --- seed: products ---
        if Product.query.count() == 0:
            db.session.add_all([
                Product(name="Apple", category="fruit", price=1000),
                Product(name="Banana", category="fruit", price=1200),
                Product(name="Carrot", category="vegetable", price=900),
                Product(name="Milk", category="dairy", price=1800),
            ])

        db.session.commit()
        print("[OK] DB initialized.")

if __name__ == "__main__":
    # 환경변수로 리셋 제어 가능 (선택)
    # RESET_DB=0 이면 drop_all 생략
    reset_flag = os.environ.get("RESET_DB", "1") != "0"
    init_db(reset=reset_flag)