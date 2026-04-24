# E-Commerce Analytics Dashboard

## Run Instructions

1. Install dependencies:
pip install -r requirements.txt

2. Generate dataset:
python data/generate_data.py

3. Run backend:
uvicorn backend.app:app --reload

4. Run dashboard:
streamlit run dashboard/streamlit_app.py
