from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('student_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        reading = float(request.form['reading'])
        writing = float(request.form['writing'])

        prediction = model.predict([[reading, writing]])

        return render_template('index.html',
                               prediction_text=f"Predicted Math Score: {prediction[0]:.2f}")
    except:
        return render_template('index.html',
                               prediction_text="⚠ Invalid Input")

if __name__ == "__main__":
    app.run(debug=True)