# ML-IDS-Machine-Learning-Enhanced-Intrusion-Detection-System
An intelligent cybersecurity solution that uses machine learning to detect network intrusions by analyzing Snort logs and the CICIDS2017 dataset. This project is ideal for roles like SOC Analyst, Security Analyst, and those entering the cyber threat detection field.

## 📌 Features
. 📥 Parses Snort alert logs and CICIDS2017 dataset\
. 🤖 Preprocesses and trains ML models (Random Forest by default)\
. 📊 Displays real-time prediction results and metrics via a Streamlit dashboard\
. 🔐 Focused on practical application for Security Operations Centers (SOCs)


## 📁 Project Structure
```
ML-IDS-Project/
├── datasets/
│   └── cicids2017.csv
├── snort_logs/
│   └── alert.log
├── scripts/
│   ├── preprocess.py
│   ├── train_model.py
│   └── detect.py
├── models/
│   └── rf_model.joblib
├── dashboard/
│   └── app.py
├── requirements.txt
└── README.md
```


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

## 📌Output 

<img width="945" height="972" alt="Screenshot 2025-07-10 190155" src="https://github.com/user-attachments/assets/8c7b8118-39e2-4e35-a7de-c0e7bc44bc13" />
<img width="933" height="776" alt="Screenshot 2025-07-10 190218" src="https://github.com/user-attachments/assets/13d4b1fd-41fc-4607-aecb-fe5e41d08414" />


## 🔬 Evaluation Metrics
. Trained on CICIDS2017 dataset:\
. Accuracy: ~99.99%\
. Precision: 1.0\
. Recall: 1.0\
. F1-Score: 1.0\
Model performs exceptionally well on balanced and unbalanced classes due to ensemble learning and feature diversity.


## 🧪 Evaluation & Testing

. After running the training and dashboard modules, evaluate the model using:\
. Classification Report\
. Accuracy/F1-score\
. Live attack simulation using Snort logs

## 🛡️ Security Features & Suggestions

. Snort-based signature detection\
. ML-enhanced behavioral detection\
. Model can be extended with:\
. Online learning\
. Deep anomaly detection (LSTM/Autoencoders)\
. Real-time packet capture with ``scapy``\
. API-based log feeding (e.g., ELK/Suricata integration)

## 📄 License
 MIT License


