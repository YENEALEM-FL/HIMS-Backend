import unittest
from db.connection import SessionLocal, engine
from models.user_model import Base, User
from services.user_service import UserService

class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create tables if not exist
        Base.metadata.create_all(bind=engine)

    def setUp(self):
        # Clean User table before each test
        self.session = SessionLocal()
        self.session.query(User).delete()
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        data = {"name": "John", "email": "john@example.com"}
        created = UserService.create_user(data)
        self.assertIsNotNone(created.get("id"))
        self.assertEqual(created["name"], "John")
        self.assertEqual(created["email"], "john@example.com")

    def test_get_all_users(self):
        UserService.create_user({"name": "A", "email": "a@test.com"})
        UserService.create_user({"name": "B", "email": "b@test.com"})
        users = UserService.get_all_users()
        self.assertEqual(len(users), 2)
        self.assertListEqual([u["name"] for u in users], ["A", "B"])

    def test_get_user(self):
        created = UserService.create_user({"name": "Test", "email": "t@test.com"})
        user_id = created["id"]
        found = UserService.get_user(user_id)
        self.assertIsNotNone(found)
        self.assertEqual(found["email"], "t@test.com")

    def test_get_user_not_found(self):
        result = UserService.get_user(999)
        self.assertIsNone(result)

    def test_update_user(self):
        created = UserService.create_user({"name": "Old", "email": "old@test.com"})
        user_id = created["id"]
        updated = UserService.update_user(user_id, {"name": "New", "email": "new@test.com"})
        self.assertIsNotNone(updated)
        self.assertEqual(updated["name"], "New")
        self.assertEqual(updated["email"], "new@test.com")

    def test_update_user_not_found(self):
        result = UserService.update_user(999, {"name": "X", "email": "x@test.com"})
        self.assertIsNone(result)

    def test_delete_user(self):
        created = UserService.create_user({"name": "Del", "email": "del@test.com"})
        user_id = created["id"]
        response = UserService.delete_user(user_id)
        self.assertEqual(response, {"message": "User deleted"})
        # Confirm deletion
        self.assertIsNone(UserService.get_user(user_id))


if __name__ == "__main__":
    unittest.main()