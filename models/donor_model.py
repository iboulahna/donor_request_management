# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Donor(db.Model):
#     __tablename__ = 'donors'

#     id = db.Column(db.Integer, primary_key=True)  # Primary key (auto-increment)
#     first_name = db.Column(db.String(100), nullable=False)
#     last_name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     phone_number = db.Column(db.String(20))
#     monthly_donation = db.Column(db.Float, nullable=False, default=0.0)  # Default value for donations
#     donation_status = db.Column(db.String(50), default="active")  # Status of the donation (e.g., "active", "paused", "cancelled")
#     created_at = db.Column(db.DateTime, server_default=db.func.now())  # Timestamp of when the donor was added
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())  # Timestamp for updates

#     def __repr__(self):
#         return f"<Donor {self.first_name} {self.last_name}>"

#     def to_dict(self):
#         """ Convert Donor object to dictionary format for easy JSON serialization """
#         return {
#             'id': self.id,
#             'first_name': self.first_name,
#             'last_name': self.last_name,
#             'email': self.email,
#             'phone_number': self.phone_number,
#             'monthly_donation': self.monthly_donation,
#             'donation_status': self.donation_status,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at
#         }

#     @classmethod
#     def find_by_email(cls, email):
#         """ Find a donor by their email address """
#         return cls.query.filter_by(email=email).first()

#     @classmethod
#     def find_by_id(cls, donor_id):
#         """ Find a donor by their ID """
#         return cls.query.get(donor_id)

#     def save(self):
#         """ Save the donor to the database """
#         db.session.add(self)
#         db.session.commit()

#     def update(self, **kwargs):
#         """ Update donor attributes """
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#         db.session.commit()

#     def delete(self):
#         """ Delete the donor from the database """
#         db.session.delete(self)
#         db.session.commit()


from mongoengine import Document, StringField, FloatField, DateTimeField, EnumField, EmailField
import datetime

class Donor(Document):
    first_name = StringField(required=True, max_length=100)
    last_name = StringField(required=True, max_length=100)
    email = EmailField(unique=True, required=True)
    phone_number = StringField(max_length=20)
    monthly_donation = FloatField(required=True, default=0.0)
    donation_status = EnumField(choices=["active", "paused", "cancelled"], default="active")
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    def to_dict(self):
        """ Convert Donor object to dictionary format for easy JSON serialization """
        return {
            'id': str(self.id),  # MongoDB uses ObjectId, convert to string
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'monthly_donation': self.monthly_donation,
            'donation_status': self.donation_status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def save(self):
        """ Save the donor to the database """
        self.save()

    def update(self, **kwargs):
        """ Update donor attributes """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def delete(self):
        """ Delete the donor from the database """
        self.delete()


# Configuration Example (in app.py or config.py):

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your_database_name'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# 3. Donor Model Use Cases
# In your application, you would typically interact with the Donor model for tasks like:

# Storing donor data when they sign up or make a donation.

# Tracking donation history and updating donation amounts.

# Suspending or resuming donations based on donor preferences (e.g., suspending donations during a temporary pause or resuming them).

# Querying donor information based on email or other fields to personalize responses or manage donor relationships.

# 4. Interactions with Other Services
# Speech-to-Text: Once the donor’s request is transcribed using AWS Transcribe, you could extract relevant donor information (such as their name or donation preferences) and update the Donor model accordingly.

# GPT-4 Query Handling: When the AI model responds to the donor's query, you can use the Donor model to fetch the donor’s history, status, or preferences to provide personalized responses.

