from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb+srv://joesa73:wq3DNdfxDtJKv6@digitalassets.9rfsg.mongodb.net/?retryWrites=true&w=majority&appName=digitalassets', server_api=ServerApi('1'))
db = client['service_requests_db']
collection = db['requests']

@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    
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
