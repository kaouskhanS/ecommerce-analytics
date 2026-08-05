# 🛒 E-Commerce Customer Churn Analytics & Prediction

An end-to-end Machine Learning project that analyzes customer behavior and predicts customer churn using Python, FastAPI, and Streamlit.

---

## 📌 Project Overview

Customer churn is one of the biggest challenges for e-commerce businesses. This project helps businesses identify customers who are likely to stop purchasing by analyzing historical customer data and predicting churn using a Machine Learning model.

The project includes:

- Customer Data Generation
- Exploratory Data Analysis (EDA)
- Machine Learning Model Training
- FastAPI REST API
- Interactive Streamlit Dashboard

---

## ✨ Features

- 📊 Customer Churn Prediction
- 📈 Interactive Business Analytics Dashboard
- 🤖 Machine Learning Classification Model
- 🔍 Customer Behavior Analysis
- ⚡ FastAPI REST API
- 📉 Churn Probability Prediction
- 🐳 Docker Support

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.x

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn
- Streamlit

### Backend
- FastAPI
- Uvicorn

### Containerization
- Docker
- Docker Compose

---

## 📂 Project Structure

```
ecommerce-analytics-main/
│
├── analysis/
│   └── churn_analysis.py
│
├── backend/
│   ├── app.py
│   └── model.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── data/
│   └── generate_data.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-analytics.git

cd ecommerce-analytics-main
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1. Generate Dataset

```bash
python data/generate_data.py
```

### 2. Perform Customer Churn Analysis

```bash
python analysis/churn_analysis.py
```

### 3. Start FastAPI Server

```bash
uvicorn backend.app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

### 4. Launch Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

---

## 📊 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Customer Churn Prediction
- Dashboard Visualization

---

## 📈 Model Evaluation Metrics

The model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## 📊 Dashboard Features

- Customer Overview
- Churn Distribution
- Customer Segmentation
- Feature Importance
- Prediction Interface
- Business Insights

---

## 🚀 Future Enhancements

- Deep Learning Model
- XGBoost & LightGBM Integration
- Real-Time Prediction
- Database Integration (MySQL/PostgreSQL)
- Cloud Deployment (AWS, Azure, GCP)
- User Authentication
- Email Notifications

---

## 📸 Screenshots

Add screenshots of:

- Streamlit Dashboard
- Customer Churn Prediction Page
- FastAPI Swagger UI
- Data Visualization Charts

---

## 📦 Docker Support

Build Docker Image

```bash
docker build -t ecommerce-analytics .
```

Run Docker Container

```bash
docker-compose up
```

---

## 🎯 Use Cases

- Customer Retention Analysis
- Customer Churn Prediction
- Marketing Strategy Optimization
- Business Intelligence
- Sales Analytics
- Customer Segmentation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Create a Pull Request.

---

## 📄 License

This project is developed for educational and portfolio purposes.

---

## 👨‍💻 Author

**Kaous Khan S and Sujitha A**

**Bachelor of Technology(ArtificialIntelligenceandDataScience)**

**Mailam Engineering College**

📧 Email: aziskhan7023@gmail.com and suji2003kk@gmail.com


🔗 GitHub: https://github.com/your-github-kaouskhanS,https://github.com/your-github-sujitha3arumugam
🔗 LinkedIn profile : https://www.linkedin.com/in/kaouskhans, https://www.linkedin.com/in/sujitha-arumugam-

## Run Instructions

1. Install dependencies:
pip install -r requirements.txt

2. Generate dataset:
python data/generate_data.py

3. Run backend:
uvicorn backend.app:app --reload

4. Run dashboard:
streamlit run dashboard/streamlit_app.py
