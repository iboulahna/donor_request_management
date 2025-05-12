### **3. Flask API for Query Management**


from flask import Flask, request, jsonify

app = Flask(__name__)

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