
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/crm/leads', methods=['POST'])
def receive_lead():
    data = request.json
    print(f"Received lead: {data}")
    return jsonify({"status": "success", "message": "Lead received"}), 200

if __name__ == '__main__':
    app.run(port=5001)
