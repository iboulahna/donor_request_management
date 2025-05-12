from flask_pymongo import PyMongo

mongo = PyMongo()

class Donor:
    def __init__(self, first_name, last_name, email, phone_number=None, total_donations=0.0, monthly_donations=0.0, status="active"):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.total_donations = total_donations
        self.monthly_donations = monthly_donations
        self.status = status

    def save(self):
        """Method to save the donor to the database."""
        donor_data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "total_donations": self.total_donations,
            "monthly_donations": self.monthly_donations,
            "status": self.status
        }
        mongo.db.donors.insert_one(donor_data)

    @classmethod
    def find_by_email(cls, email):
        """Method to find a donor by email."""
        donor_data = mongo.db.donors.find_one({"email": email})
        if donor_data:
            return cls(**donor_data)
        return None

    def update_donations(self, donation_amount):
        """Update total and monthly donations."""
        self.total_donations += donation_amount
        self.monthly_donations = donation_amount
        mongo.db.donors.update_one({"email": self.email}, {"$set": {"total_donations": self.total_donations, "monthly_donations": self.monthly_donations}})

    def suspend_donations(self):
        """Suspend the donor's monthly donations."""
        self.status = "suspended"
        mongo.db.donors.update_one({"email": self.email}, {"$set": {"status": self.status}})

    def resume_donations(self):
        """Resume the donor's donations."""
        self.status = "active"
        mongo.db.donors.update_one({"email": self.email}, {"$set": {"status": self.status}})

# Configuration Example (in app.py or config.py):

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your_database_name'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
