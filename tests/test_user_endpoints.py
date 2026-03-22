import unittest
from sqlalchemy.exc import IntegrityError
from db.connection import Base, engine, SessionLocal
from models.user_model import User  # adjust path if needed


class TestUserModel(unittest.TestCase):

    def setUp(self):
        # Create tables (if not exist)
        Base.metadata.create_all(bind=engine)
        self.session = SessionLocal()

    def tearDown(self):
        # Clean up test data
        self.session.query(User).delete()
        self.session.commit()
        self.session.close()

    def test_create_user(self):
        user = User(name="John Doe", email="john_test@example.com")
        self.session.add(user)
        self.session.commit()

        result = self.session.query(User).filter_by(email="john_test@example.com").first()

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, "John Doe")
        self.assertEqual(result.email, "john_test@example.com")

    def test_unique_email_constraint(self):
        user1 = User(name="John", email="duplicate@example.com")
        user2 = User(name="Jane", email="duplicate@example.com")

        self.session.add(user1)
        self.session.commit()

        self.session.add(user2)

        with self.assertRaises(IntegrityError):
            self.session.commit()

        self.session.rollback()

    def test_to_dict(self):
        user = User(name="Alice", email="alice_test@example.com")
        self.session.add(user)
        self.session.commit()

        result = user.to_dict()

        self.assertIn("id", result)
        self.assertEqual(result["name"], "Alice")
        self.assertEqual(result["email"], "alice_test@example.com")


if __name__ == "__main__":
    unittest.main()