import unittest
from db.connection import SessionLocal, engine
from models.user_model import Base, User
from repositories.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Create all tables in the database before running any tests.
        This uses the preconfigured MySQL engine.
        """
        Base.metadata.create_all(bind=engine)

    def setUp(self):
        """
        Clean the User table before each test.
        """
        self.session = SessionLocal()
        # Delete all rows to start with a clean state
        self.session.query(User).delete()
        self.session.commit()

    def tearDown(self):
        """
        Close the session after each test.
        """
        self.session.close()

    def test_create_user(self):
        user = User(name="John", email="john@example.com")
        created = UserRepository.create(user)
        self.assertIsNotNone(created.id)
        self.assertEqual(created.name, "John")
        self.assertEqual(created.email, "john@example.com")

    def test_find_all(self):
        UserRepository.create(User(name="A", email="a@test.com"))
        UserRepository.create(User(name="B", email="b@test.com"))
        users = UserRepository.find_all()
        self.assertEqual(len(users), 2)

    def test_find_by_id(self):
        user = UserRepository.create(User(name="Test", email="t@test.com"))
        found = UserRepository.find_by_id(user.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.email, "t@test.com")

    def test_update_user(self):
        user = UserRepository.create(User(name="Old", email="old@test.com"))
        updated = UserRepository.update(user.id, {
            "name": "New",
            "email": "new@test.com"
        })
        self.assertIsNotNone(updated)
        self.assertEqual(updated.name, "New")
        self.assertEqual(updated.email, "new@test.com")

    def test_update_user_not_found(self):
        result = UserRepository.update(999, {
            "name": "X",
            "email": "x@test.com"
        })
        self.assertIsNone(result)

    def test_delete_user(self):
        user = UserRepository.create(User(name="Del", email="del@test.com"))
        UserRepository.delete(user.id)
        result = UserRepository.find_by_id(user.id)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()