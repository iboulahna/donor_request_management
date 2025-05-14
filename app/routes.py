### **3. Flask API for Query Management**


from flask import Flask, request, jsonify
from app.models.donor_model import Donor

app = Flask(__name__)


@app.route('/add_donor', methods=['POST'])
def add_donor():
    data = request.json
    donor = Donor(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone_number=data.get('phone_number'),
        monthly_donation=data['monthly_donation'],
    )
    donor.save()
    return jsonify(donor.to_dict()), 201

@app.route('/donor/<email>', methods=['GET'])
def get_donor_by_email(email):
    donor = Donor.find_by_email(email)
    if donor:
        return jsonify(donor.to_dict())
    return jsonify({"message": "Donor not found"}), 404


@app.route('/handle_request', methods=['POST'])
def handle_request():
    data = request.json
    user_query = data.get("query")
    response = generate_response(user_query)

    if "complex" in response:
        return jsonify({"response": "This request will be transferred to an advisor."})
    else:
        return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

