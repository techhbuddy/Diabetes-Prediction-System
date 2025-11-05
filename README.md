# PredictDia : Diabetes Prediction System

A web-based machine learning application for predicting diabetes using patient medical data. The system uses a trained ML model (Logistic Regression by default) and provides a user-friendly interface to enter patient details and receive instant predictions.

## Features

- **ML-powered backend:** Predicts diabetes based on medical input data.
- **Web UI:** Simple, clean form for data entry and immediate results.
- **Data Preprocessing:** Input data is standardized to match the model's expectations.
- **Ready to Deploy:** Easy to run locally or host on any Python-compatible server.

## Project Structure

```
diabetes-prediction-system/
├── diabetes.csv
├── Diabetes_Prediction.ipynb
├── model.pkl
├── scaler.pkl
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
```

## Installation & Running

### 1. Clone the Repository

```bash
git clone https://github.com/techhbuddy/Diabetes-Prediction-System.git
cd Diabetes-Prediction-System
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model (If model.pkl and scaler.pkl don't exist)

```bash
python Diabetes_Prediction.ipynb
```
This will create `model.pkl` and `scaler.pkl` in your directory.

### 5. Run the Web App

```bash
python app.py
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## Usage

1. Open the web UI.
2. Fill in patient details such as Pregnancies, Glucose, Blood Pressure, etc.
3. Click "Predict" to see if diabetes is detected or not, along with the probability.

---

## File Descriptions

- **diabetes.csv**: The dataset used for training the model.
- **Diabetes_Prediction.ipynb**: Script to train the machine learning model and save it.
- **model.pkl, scaler.pkl**: The trained model and scaler, used for predictions.
- **app.py**: Flask application to serve the web interface and prediction API.
- **templates/index.html**: The HTML front-end for user input.
- **requirements.txt**: List of Python dependencies.

---

## Customization

- **Change the model:** Edit `train_model.py` to use another scikit-learn classifier if desired.
- **UI improvements:** Modify `templates/index.html` for a better look and feel.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

*For questions or suggestions, please open an issue or contact the maintainer.*
