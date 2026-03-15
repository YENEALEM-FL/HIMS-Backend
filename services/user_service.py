from repositories.user_repository import UserRepository
from models.user_model import User

class UserService:

    @staticmethod
    def get_all_users():
        return [u.to_dict() for u in UserRepository.find_all()]

    @staticmethod
    def get_user(user_id):
        user = UserRepository.find_by_id(user_id)
        return user.to_dict() if user else None

    @staticmethod
    def create_user(data):
        user = User(name=data["name"], email=data["email"])
        created = UserRepository.create(user)
        return created.to_dict()

    @staticmethod
    def update_user(user_id, data):
        updated = UserRepository.update(user_id, data)
        return updated.to_dict() if updated else None

    @staticmethod
    def delete_user(user_id):
        UserRepository.delete(user_id)
        return {"message": "User deleted"}
