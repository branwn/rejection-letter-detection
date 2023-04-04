from flask import Flask, abort, request, render_template, jsonify
from tempfile import NamedTemporaryFile
import torch
import joblib

def getSpam(emailContent):
    clf = joblib.load('trained_model_1.pkl')
    return str(clf.predict([emailContent])[0])


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api', methods=['POST'])
def process_text():
    # Get the posted text (assuming the field name is "text-input")
    text_input = request.form.get('text-input')
    
    # Print the received text (optional)
    print("Received text:", text_input)

    res = "non-Rejucted"

    if getSpam(text_input) == "1":
        res = "Rejucted"


    # Return "accept" each time
    response = {
        'status': res
    }

    return jsonify(response)



