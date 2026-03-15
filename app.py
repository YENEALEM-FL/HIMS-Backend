# app.py
from flask import Flask
from db.connection import engine, Base
from routes.user_routes import users_bp

app = Flask(__name__)

# ⚡ Create tables automatically before using blueprint
Base.metadata.create_all(bind=engine)

# Register blueprint
app.register_blueprint(users_bp, url_prefix="/users")

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)