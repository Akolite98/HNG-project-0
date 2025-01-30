from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_info():
    # Replace with your registered email
    email = "nnorompreciousakachukwu@gmail.com"
    
    # Get current datetime in ISO 8601 format (UTC)
    current_datetime = datetime.utcnow().isoformat() + "Z"
    
    # Replace with your GitHub repository URL
    github_url = "https://github.com/Akolite98/HNG-project-0"
    
    # Return JSON response
    return jsonify({
        "email": email,
        "current_datetime": current_datetime,
        "github_url": github_url
    })

if __name__ == '__main__':
    app.run()