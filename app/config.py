# In app/config.py

# # For SQLAlchemy (PostgreSQL):

# class Config:
#     SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/donor_db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = 'your-secret-key'

#  in Mongo db 

class Config:
    MONGO_URI = 'mongodb://localhost:27017/donor_db'
    SECRET_KEY = 'your-secret-key'
