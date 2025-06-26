from flask import Flask, render_template, request
import os
import pandas as pd
import pickle
from werkzeug.utils import secure_filename

app = Flask(__name__)
MODEL_PATH = "anomaly_model.pkl"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file_path = os.path.join("uploads", filename)
        os.makedirs("uploads", exist_ok=True)
        file.save(file_path)

        # Load model, scaler and encoders
        with open(MODEL_PATH, "rb") as f:
            model, scaler, label_encoders = pickle.load(f)

        df = pd.read_csv(file_path)

        # Datetime processing
        for col in ['creation_time', 'end_time', 'time']:
            df[col] = pd.to_datetime(df[col], errors='coerce')

        df['hour'] = df['time'].dt.hour
        df['dayofweek'] = df['time'].dt.dayofweek
        df['duration_sec'] = (df['end_time'] - df['creation_time']).dt.total_seconds()

        # Encode with saved LabelEncoders
        for col, le in label_encoders.items():
            if col in df.columns:
                df[col] = le.transform(df[col].astype(str))

        df_proc = df.drop(columns=['creation_time', 'end_time', 'time'])
        scaled = scaler.transform(df_proc)

        df['anomaly'] = model.predict(scaled)
        df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

        anomalies = df[df['anomaly'] == 1]
        output_path = os.path.join("uploads", f"anomaly_{filename}")
        df.to_csv(output_path, index=False)

        #return render_template("index.html", tables=[df.to_html(classes="data", index=False)], anomaly_count=len(anomalies))
        return render_template("index.html", tables=[anomalies.to_html(classes="data", index=False)], anomaly_count=len(anomalies))


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
