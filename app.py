from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
import joblib


app = Flask(__name__)

# Load the model using joblib
model = joblib.load('model_pipeline.pkl')
# Define the expected columns
cols = ['credit_history', 'purpose', 'credit_amount', 'savings_account', 'personal_status_and_sex', 'job']


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features).reshape(1, -1)
    data_unseen = pd.DataFrame(final, columns=cols)
    prediction = model.predict(data_unseen)
    return render_template('home.html', pred='Expected outcome is {}'.format(prediction[0]))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = model.predict(data_unseen)
    return jsonify(prediction[0])

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=config.PORT, debug=config.DEBUG_MODE)