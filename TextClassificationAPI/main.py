from flask import Flask, request, jsonify
from service.TextClassification import modelPrediction
import os
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
        return jsonify({"Text": "Hello"})


@app.route('/textClassification', methods=['POST'])
def text_Classification():
    try:
        data = request.get_json()
        text = data['text']
        result = modelPrediction(text)
        print(result)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT',8080)))
