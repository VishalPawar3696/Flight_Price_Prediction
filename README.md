# ✈️ Flight Price Predictor

A Streamlit web app that predicts flight prices based on user input such as airline, source, destination, date, and duration. Powered by a machine learning model trained using scikit-learn.

---

## 🔧 Project Structure

flight_price_predictor/

├── app.py # Streamlit app

├── flight_price_model.pkl # Trained ML model

├── preprocessing.py # Data preprocessing functions

├── requirements.txt # Python dependencies

└── README.md # Project documentation


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flight-price-predictor.git
cd flight-price-predictor

python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

📥 User Input
Airline: Dropdown (e.g., IndiGo, Air India)

Source: Dropdown (e.g., Delhi, Mumbai)

Destination: Dropdown (e.g., Cochin, Kolkata)

Flight Date: Date picker

Duration: Text input (e.g., "2h 30m")

📦 Requirements
streamlit
pandas
scikit-learn
joblib

📌 Notes
The model file flight_price_model.pkl must be in the project directory.

Ensure preprocessing.py contains a preprocess_input function that transforms user input to the model’s expected format.

![Screenshot (64)](https://github.com/user-attachments/assets/d7a33af2-f482-4293-94d0-0e91d806d1a9)
![Screenshot (65)](https://github.com/user-attachments/assets/fa46c105-bfe4-4f29-a276-2240ff663203)


![Screenshot (66)](https://github.com/user-attachments/assets/fee0ca96-8c23-4422-8e26-1e9978d2409c)
![Screenshot (67)](https://github.com/user-attachments/assets/a3d002a1-2ae0-4d93-bcbe-b593234f0d22)


---
email: vishalpawar3696@gmail.com
Let me know if you’d like me to generate `preprocessing.py` or help with `app.py` content too.
