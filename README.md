# Cybersecurity_Anomaly_Detection
# 🚨 Network Traffic Anomaly Detection with Flask

This project is a machine learning-powered web application that detects anomalies in network traffic logs using an Isolation Forest model. It provides a user-friendly interface to upload a CSV file, automatically detect unusual activity, and download a cleaned report of anomalies.

## 🔧 Features

- Upload raw network traffic CSVs via the browser
- Automatically:
  - Clean blank or malformed rows
  - Parse datetime columns
  - Extract time-based features (`hour`, `dayofweek`, `duration`)
  - Encode categorical variables
  - Scale features using StandardScaler
  - Detect anomalies using Isolation Forest
- View results in-browser
- Download the cleaned output with anomalies labeled

---

## 💡 How It Works

### Model Training 

- Preprocess the CSV:
  - Drop malformed rows
  - Convert times
  - Extract features
  - Encode categories
- Train `IsolationForest` to detect outliers
- Save both model and scaler using `pickle`

### Flask App

- Load model and scaler at runtime
- Accept user CSVs
- Apply the same preprocessing pipeline
- Predict anomalies
- Return results 

### AI Tools Used

- ChatGPT - Used for code generation, debugging, and explanation.
- NotebookLM - Used for analyzing dataset and documents.
- Napkin.io - Used for Visualizing data.


🔮 Future Enhancements
1. Real-time Anomaly Detection
2. Downloadable Detailed PDF Reports
3. Multiclass Anomaly Categorization
4. Alert System
