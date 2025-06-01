# Import necessary libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model_filename = 'xgb_model.sav'  # Update with the correct model file (e.g., rf_model.sav or lr_model.sav)
try:
    model = pickle.load(open(model_filename, 'rb'))
except FileNotFoundError:
    print(f"Error: Model file '{model_filename}' not found. Please ensure the model is saved correctly.")
    exit(1)

# Initialize LabelEncoders for categorical features
le_quarter = LabelEncoder()
le_department = LabelEncoder()
le_day = LabelEncoder()

# Fit LabelEncoders with the same categories as used during training
le_quarter.fit(['Quarter1', 'Quarter2', 'Quarter3', 'Quarter4', 'Quarter5'])
le_department.fit(['sweing', 'finishing'])
le_day.fit(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Retrieve form data
        quarter = request.form['quarter']
        department = request.form['department']
        day = request.form['day']
        team = float(request.form['team'])
        targeted_productivity = float(request.form['targeted_productivity'])
        smv = float(request.form['smv'])
        wip = float(request.form['wip'])
        over_time = float(request.form['over_time'])
        incentive = float(request.form['incentive'])
        idle_time = float(request.form['idle_time'])
        idle_men = float(request.form['idle_men'])
        no_of_style_change = float(request.form['no_of_style_change'])
        no_of_workers = float(request.form['no_of_workers'])
        month = float(request.form['month'])

        # Encode categorical features
        quarter_encoded = le_quarter.transform([quarter])[0]
        department_encoded = le_department.transform([department])[0]
        day_encoded = le_day.transform([day])[0]

        # Prepare input array for prediction
        input_data = np.array([[
            quarter_encoded, department_encoded, day_encoded, team, targeted_productivity,
            smv, wip, over_time, incentive, idle_time, idle_men, no_of_style_change,
            no_of_workers, month
        ]])

        # Make prediction
        prediction = model.predict(input_data)[0]

        # Render the result on submit.html
        return render_template('submit.html', prediction=round(prediction, 4))

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)