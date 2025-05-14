# from flask_pymongo import PyMongo

# mongo = PyMongo()

# class Donor:
#     def __init__(self, first_name, last_name, email, phone_number=None, total_donations=0.0, monthly_donations=0.0, status="active"):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone_number = phone_number
#         self.total_donations = total_donations
#         self.monthly_donations = monthly_donations
#         self.status = status

#     def save(self):
#         """Method to save the donor to the database."""
#         donor_data = {
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "email": self.email,
#             "phone_number": self.phone_number,
#             "total_donations": self.total_donations,
#             "monthly_donations": self.monthly_donations,
#             "status": self.status
#         }
#         mongo.db.donors.insert_one(donor_data)

#     @classmethod
#     def find_by_email(cls, email):
#         """Method to find a donor by email."""
#         donor_data = mongo.db.donors.find_one({"email": email})
#         if donor_data:
#             return cls(**donor_data)
#         return None

#     def update_donations(self, donation_amount):
#         """Update total and monthly donations."""
#         self.total_donations += donation_amount
#         self.monthly_donations = donation_amount
#         mongo.db.donors.update_one({"email": self.email}, {"$set": {"total_donations": self.total_donations, "monthly_donations": self.monthly_donations}})

#     def suspend_donations(self):
#         """Suspend the donor's monthly donations."""
#         self.status = "suspended"
#         mongo.db.donors.update_one({"email": self.email}, {"$set": {"status": self.status}})

#     def resume_donations(self):
#         """Resume the donor's donations."""
#         self.status = "active"
#         mongo.db.donors.update_one({"email": self.email}, {"$set": {"status": self.status}})

# from mongoengine import Document, StringField, FloatField, DateTimeField, EnumField, EmailField
# import datetime

# class Donor(Document):
#     first_name = StringField(required=True, max_length=100)
#     last_name = StringField(required=True, max_length=100)
#     email = EmailField(unique=True, required=True)
#     phone_number = StringField(max_length=20)
#     monthly_donation = FloatField(required=True, default=0.0)
#     donation_status = EnumField(choices=["active", "paused", "cancelled"], default="active")
#     created_at = DateTimeField(default=datetime.datetime.utcnow)
#     updated_at = DateTimeField(default=datetime.datetime.utcnow)

#     def to_dict(self):
#         """ Convert Donor object to dictionary format for easy JSON serialization """
#         return {
#             'id': str(self.id),  # MongoDB uses ObjectId, convert to string
#             'first_name': self.first_name,
#             'last_name': self.last_name,
#             'email': self.email,
#             'phone_number': self.phone_number,
#             'monthly_donation': self.monthly_donation,
#             'donation_status': self.donation_status,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at
#         }

#     def save(self):
#         """ Save the donor to the database """
#         self.save()

#     def update(self, **kwargs):
#         """ Update donor attributes """
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#         self.save()

#     def delete(self):
#         """ Delete the donor from the database """
#         self.delete()

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

