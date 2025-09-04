import os

class Config:
    # PostgreSQL Database URI
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:1122@localhost:5432/smart_apply_system"


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
