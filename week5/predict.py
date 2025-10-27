import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = "model_C=1.0.bin"

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


app = Flask('churn')


# docker build -t flask-churn -f week5/Dockerfile .
#  docker run -it --rm -p 9696:9696 flask-churn

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': y_pred,
        'churn': bool(churn)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
