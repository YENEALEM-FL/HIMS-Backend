import unittest
from unittest.mock import patch
from flask import Flask, json
from routes.user_routes import users_bp  # your blueprint file


class TestUserRoutes(unittest.TestCase):

    def setUp(self):
        # Create a Flask app and register the blueprint
        self.app = Flask(__name__)
        self.app.register_blueprint(users_bp, url_prefix="/users")
        self.client = self.app.test_client()

    @patch("routes.user_routes.UserService.get_all_users")
    def test_get_all_users(self, mock_get_all):
        mock_get_all.return_value = [{"id": 1, "name": "John", "email": "john@example.com"}]

        response = self.client.get("/users/")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "John")

    @patch("routes.user_routes.UserService.get_user")
    def test_get_user(self, mock_get_user):
        mock_get_user.return_value = {"id": 1, "name": "John", "email": "john@example.com"}

        response = self.client.get("/users/1")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 1)

    @patch("routes.user_routes.UserService.create_user")
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = {"id": 1, "name": "John", "email": "john@example.com"}

        response = self.client.post("/users/", json={"name": "John", "email": "john@example.com"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["name"], "John")

    @patch("routes.user_routes.UserService.update_user")
    def test_update_user(self, mock_update_user):
        mock_update_user.return_value = {"id": 1, "name": "New", "email": "new@example.com"}

        response = self.client.put("/users/1", json={"name": "New", "email": "new@example.com"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], "New")

    @patch("routes.user_routes.UserService.delete_user")
    def test_delete_user(self, mock_delete_user):
        mock_delete_user.return_value = {"message": "User deleted"}

        response = self.client.delete("/users/1")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "User deleted")


if __name__ == "__main__":
    unittest.main()