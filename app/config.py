# In app/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/donor_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
