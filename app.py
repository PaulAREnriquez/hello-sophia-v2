from flask import Flask, render_template, request, jsonify
from flask_cors import CORS # pip install cors
from chat import get_response

app = Flask(__name__)
CORS(app) # to allow cross-origin sharing

# Uncomment this if you want to run it not as a standalone application
"""
@app.get("/")
def index_get():
    return render_template('base.html')    
"""

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: you can check if text is valid json
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)