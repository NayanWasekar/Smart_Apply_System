import os
from datetime import timedelta

class Config:
    # PostgreSQL Database URI
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:1122@localhost:5432/smart_apply_system"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret key for session & JWT
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    # JWT configuration
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")  # Secret key for JWT signing
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)  # Access token expiry (default: 15 mins)
    #JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)     # Refresh token expiry (default: 7 days)
    JWT_TOKEN_LOCATION = ["headers"]  # You can also allow cookies: ["headers", "cookies"]
    JWT_HEADER_TYPE = "Bearer"        # Token type in Authorization header
