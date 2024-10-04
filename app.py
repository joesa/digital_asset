from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True, resources={r"/*": {"origins": "*"}})


# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['service_requests_db']
collection = db['requests']

@app.route('/submit-form', methods=['POST'])
def submit_form():
    print("Hello App!")
    data = request.get_json()
    print(data['name'])
    print(data['email'])
    # Validate data
    if not all(k in data for k in ('name', 'phone', 'email', 'serviceType')):
        return jsonify({'error': 'Missing data fields'}), 400
    
    # Store data in MongoDB
    collection.insert_one({
        'name': data['name'],
        'phone': data['phone'],
        'email': data['email'],
        'service_type': data['serviceType']
    })
    
    return jsonify({'message': 'Form submitted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
