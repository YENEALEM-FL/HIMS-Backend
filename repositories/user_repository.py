from db.connection import SessionLocal
from models.user_model import User

class UserRepository:

    @staticmethod
    def find_all():
        with SessionLocal() as session:
            return session.query(User).all()

    @staticmethod
    def find_by_id(user_id):
        with SessionLocal() as session:
            return session.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(user: User):
        with SessionLocal() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    @staticmethod
    def update(user_id, data):
        with SessionLocal() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                return None
            user.name = data["name"]
            user.email = data["email"]
            session.commit()
            session.refresh(user)
            return user

    @staticmethod
    def delete(user_id):
        with SessionLocal() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
