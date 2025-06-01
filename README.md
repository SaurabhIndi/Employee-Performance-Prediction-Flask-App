# Productivity Prediction Web App

This is a Flask-based web application that predicts garment worker productivity using two machine learning models: Random Forest and XGBoost. The app allows users to input features such as team, targeted productivity, standard minute value (SMV), work in progress (WIP), and more, and displays predicted productivity scores from both models. The application is deployed at [https://productivity-prediction.onrender.com](https://productivity-prediction.onrender.com).

## Features
- **Predict Productivity**: Enter worker and production details to get productivity predictions from both Random Forest and XGBoost models.
- **User-Friendly Interface**: Navigate between Home, Predict, and About pages to interact with the app.
- **Dual Model Predictions**: Compare predictions from two machine learning models for the same input.
- **Deployed on Render**: Accessible online with automatic deployment via GitHub integration.

## Project Structure
```
productivity-prediction/
│
├── templates/
│   ├── about.html        # About page
│   ├── home.html         # Home page
│   ├── predict.html      # Input form for predictions
│   ├── submit.html       # Displays prediction results
│
├── app.py                # Flask application script
├── rf_model.sav          # Random Forest model file
├── xgb_model.sav         # XGBoost model file
├── requirements.txt      # Python dependencies
├── render.yaml           # Render deployment configuration
├── .gitignore            # Git ignore file
├── screenshots/
│   ├── submit.png        # Screenshot of prediction result
```

## Dataset Features
The app uses the [Productivity Prediction of Garment Employees](https://www.kaggle.com/datasets/utkarshsarbahi/productivity-prediction-of-garment-employees) dataset. The following features are used for predictions:

- **quarter**: The quarter of the year (e.g., Quarter1, Quarter2). Categorical, indicating the time period.
- **department**: The department (`sweing` or `finishing`). Categorical, affecting productivity workflows.
- **day**: The day of the week (e.g., Monday, Thursday). Categorical, capturing weekly productivity patterns.
- **team**: The team number (1–12). Categorical, representing different work groups.
- **targeted_productivity**: The target productivity (0.35–0.8). Numerical, setting expected output.
- **smv**: Standard Minute Value (2.9–50.48). Numerical, time allocated for tasks.
- **wip**: Work in Progress (0–1591). Numerical, incomplete units; missing for `finishing`.
- **over_time**: Overtime in minutes (0–25920). Numerical, extra work hours.
- **incentive**: Incentive amount (0–98). Numerical, financial motivation.
- **idle_time**: Idle time in minutes (0–6.5). Numerical, downtime duration.
- **idle_men**: Number of idle workers (0–40). Numerical, unused labor.
- **no_of_style_change**: Number of style changes (0–2). Numerical, production changes.
- **no_of_workers**: Number of workers (2–59). Numerical, team size.
- **month**: Month derived from date (1–12). Numerical, capturing monthly trends.

The target variable, **actual_productivity** (0.2337–0.9880), is predicted by the models but not used as an input feature.

## Prerequisites
- **Python 3.10+**: Required to run the Flask app locally.
- **Git**: For cloning and managing the repository.
- **Render Account**: For deploying the app (optional).

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/productivity-prediction.git
   cd productivity-prediction
   ```
   Replace `your-username` with your GitHub username.

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App Locally**:
   ```bash
   python app.py
   ```
   - Open `http://127.0.0.1:5000` in a browser to access the app.

## Usage
1. **Home Page**: Access the app at `http://127.0.0.1:5000` (locally) or [https://productivity-prediction.onrender.com](https://productivity-prediction.onrender.com) (deployed).
2. **Predict Page**: Click "Predict" to enter input features (e.g., Quarter, Department, Team, SMV, etc.).
3. **Submit**: Enter values and click "Submit" to view predictions from both Random Forest and XGBoost models.
4. **Example Input**:
   - Quarter: Quarter1
   - Department: Sweing
   - Day: Monday
   - Team: 1
   - Targeted Productivity: 0.80
   - SMV: 26.16
   - WIP: 1100
   - Over Time: 7200
   - Incentive: 50
   - Idle Time: 0
   - Idle Men: 0
   - No of Style Change: 0
   - No of Workers: 59
   - Month: 1
   - **Example Output**:
     - Random Forest Predicted Productivity: ~0.8017
     - XGBoost Predicted Productivity: ~0.7888
   ![Prediction Result](screenshots/submit.png)

5. **About Page**: Learn more about the app’s purpose and functionality.

## Deployment on Render
The app is deployed on Render at [https://productivity-prediction.onrender.com](https://productivity-prediction.onrender.com). To deploy your own instance:

1. **Push to GitHub**:
   Ensure your repository is up-to-date:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create a Render Web Service**:
   - Log in to [render.com](https://render.com/) and connect your GitHub account.
   - Click **New > Web Service** and select your `productivity-prediction` repository.
   - Configure:
     - Environment: Python
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
     - Plan: Free
     - Auto-Deploy: Enabled
   - Click **Create Web Service**.

3. **Access the App**:
   - Once deployed, Render provides a URL (e.g., `https://productivity-prediction.onrender.com`).
   - Test the app by navigating to the Predict page and submitting inputs.

## Troubleshooting
- **Model File Errors**: Ensure `rf_model.sav` and `xgb_model.sav` are in the repository and accessible by `app.py`.
- **Dependency Issues**: Verify `requirements.txt` includes all packages (`flask`, `numpy`, `scikit-learn`, `xgboost`, `gunicorn`).
- **Prediction Discrepancies**: Confirm `LabelEncoder` categories in `app.py` match the training data.
- **Render Logs**: Check the **Logs** tab in Render’s dashboard for build or runtime errors.
- **Ephemeral File System**: Render’s free tier doesn’t persist files across deploys, but including `rf_model.sav` and `xgb_model.sav` in the repository ensures they’re available.

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your fork and create a pull request:
   ```bash
   git push origin feature/your-feature
   ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (if applicable).

## Acknowledgments
- Built using [Flask](https://flask.palletsprojects.com/), [scikit-learn](https://scikit-learn.org/), and [XGBoost](https://xgboost.readthedocs.io/).
- Dataset: [Productivity Prediction of Garment Employees](https://www.kaggle.com/datasets/utkarshsarbahi/productivity-prediction-of-garment-employees).
- Deployed on [Render](https://render.com/).