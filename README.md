# ML-IDS-Machine-Learning-Enhanced-Intrusion-Detection-System
An intelligent cybersecurity solution that uses machine learning to detect network intrusions by analyzing Snort logs and the CICIDS2017 dataset. This project is ideal for roles like SOC Analyst, Security Analyst, and those entering the cyber threat detection field.

## 📌 Features
. 📥 Parses Snort alert logs and CICIDS2017 dataset\
. 🤖 Preprocesses and trains ML models (Random Forest by default)\
. 📊 Displays real-time prediction results and metrics via a Streamlit dashboard\
. 🔐 Focused on practical application for Security Operations Centers (SOCs)

## 🛠️ Tech Stack
. Python 3.x\
. Pandas, Scikit-learn, Joblib\
. Streamlit for dashboard UI\
. Snort for generating real-time intrusion logs\
. CICIDS2017 as the labeled dataset

## ⚙️ How to Run

1.Install requirements
 ```
pip install -r requirements.txt
 ```

 2.Preprocess the dataset
 ```
 python scripts/preprocess.py
```

 3.Train the ML model
 ```
 python scripts/train_model.py
 ```

 4.Launch the dashboard
 ```
 streamlit run dashboard/app.py
```

5. (Optional) Monitor Snort alerts from
    ```
    snort_logs/alert.log
   ```


 ## 📈 Evaluation Metrics
. Accuracy: ~99.99%\
. Precision, Recall, F1-score per class\
. Confusion Matrix and Classification Report

## 👨‍🏫 Use Cases
. Real-world SOC simulation project\
. Academic demonstration of ML for security\
. Benchmarking ML models with Snort log correlation

## 📌 Future Scope

. Integrate with live packet capture tools (like tcpdump)\
. Deploy dashboard via Docker or cloud (AWS/GCP)\
. Enhance with deep learning (LSTM, autoencoders)

# 📄 License
 MIT License


