import os

class SystemConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://hogehoge:hogehoge@localhost:5432/test_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


Config = SystemConfig