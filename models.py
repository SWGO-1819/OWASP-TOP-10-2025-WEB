# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), nullable=False)  # 실습용: 평문/해시 모두 가능
    role = db.Column(db.String(20), nullable=False, default="user")  # admin/user

    def __repr__(self) -> str:
        return f"<User {self.username} ({self.role})>"


class Product(db.Model):
    """
    SQLi(Search) 데모용 테이블.
    검색/필터 기능에서 WHERE 조건을 문자열로 조립하면 취약(LOW),
    바인딩/ORM 사용하면 안전(HIGH) 시나리오로 쓰기 좋다.
    """
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    category = db.Column(db.String(40), nullable=False, index=True)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Product {self.name} {self.category} {self.price}>"