from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # pip install cors
from chat import get_response
import json

app = Flask(__name__)
CORS(app)  # to allow cross-origin sharing

# Uncomment this if you want to run it not as a standalone application
"""
@app.get("/")
def index_get():
    return render_template('base.html')    
"""


# Associates the /predict URL endpoint with the predict()
# Whenever a POST request is made to the /predict endpoint, Flask will execute the code inside the predict() function.
@app.post("/predict")
def predict():
    # request.get_json() retrieves the JSON data from the request body
    # extracts the value of the "message" key
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
