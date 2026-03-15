## ReadMe

### Flask + MySQL CRUD Backend

This backend provides full CRUD operations for a users table using:

- Python 3

- Flask

- SQLAlchemy ORM

- MySQL (version 8+)

- mysql-connector-python

- python-dotenv for environment variable management

It is designed to be simple, modular, and easy to extend.

### 📦 Required Packages

#### All dependencies are listed in requirements.txt:

'''
Flask==3.0.0
SQLAlchemy==2.0.22
mysql-connector-python==8.3.0
python-dotenv==1.0.0
'''

Install them with:

pip install -r requirements.txt

pip freeze > requirements.txt => to save the requirements for later use.

### 🗄️ MySQL Configuration

#### Database settings are loaded from the .env file:

'''
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=1234@Abcd
DB_NAME=HIMSDB
DB_PORT=3306 '''

- add PYTHONDONTWRITEBYTECODE=1 in .env file.

#### Update these values in .env if needed.

▶️ Running the Application

:\> python app.py

#### Create and activate a virtual environment:

'''
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
'''

#### Install required packages:

pip install -r requirements.txt

#### Run the Flask server:

flask run

The server will start at:

http://127.0.0.1:5000

### 📚 API Endpoints

#### GET /users

Returns all users.

#### GET /users/<id>

Returns a single user.

#### POST /users

Creates a new user.
'''
Body:

{
"name": "John Doe",
"email": "john@example.com"
}
'''

#### PUT /users/<id>

Updates a user.

#### DELETE /users/<id>

Deletes a user.

✔️ Health Check

#### GET /health

Returns:

{"status": "ok"}

### 📁 Project Structure

'''
backend/
├─ app.py # Entry point for running the application
├─ .env # Environment variables for database credentials
├─ requirements.txt # Python dependencies
├─ README.md
├─ db/ # Database connection setup
│ └─ connection.py
├─ models/ # SQLAlchemy models
│ └─ user_model.py
├─ repositories/ # Database access logic
│ └─ user_repository.py
├─ services/ # Business logic / service layer
│ └─ user_service.py
└─ routes/ # Flask route blueprints
├─ **init**.py
└─ users.py

'''

### 🧩 Notes

'''

The project uses Blueprints for clean route organization.

Environment variables are stored in .env instead of hardcoding credentials.

SQLAlchemy automatically creates the users table if it doesn’t exist.

You can easily extend this structure with more models, routes, services, or repositories.

Always activate the virtual environment before running the server.
'''
