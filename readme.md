

# 🌾 Smart Crop Recommendation System

This project is an end-to-end Machine Learning application that recommends the most suitable crop for cultivation based on soil nutrients and weather conditions. It features a **Flask web interface** and is fully **containerized using Docker** for easy deployment.

## 🚀 Key Features

* **Multi-Model Analysis:** Uses Random Forest and Decision Tree classifiers for high-accuracy predictions.
* **Web Interface:** User-friendly HTML/CSS frontend to input Nitrogen (N), Phosphorous (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.
* **Containerized:** Fully Dockerized to ensure it runs identically on any system without manual dependency installation.
* **API Support:** Built with Flask, allowing it to function as both a web app and a REST API.

## 🛠️ Tech Stack

* **Language:** Python 3.9
* **ML Libraries:** Scikit-learn, Numpy, Pandas, Pickle
* **Backend:** Flask
* **Deployment:** Docker
* **Frontend:** HTML5, CSS3

## 📦 How to Run

### Option 1: Using Docker (Recommended)

1. **Build the Image:**
```bash
docker build -t crop-app .

```


2. **Run the Container:**
```bash
docker run -p 5000:5000 crop-app

```


3. **Access the App:** Open `http://localhost:5000` in your browser.

### Option 2: Local Installation

1. Install dependencies: `pip install -r requirements.txt`.
2. Run the app: `python app.py`.

## 📊 Dataset Features

The model accepts 7 key environmental parameters:

* **N-P-K:** Nitrogen, Phosphorous, and Potassium content in soil.
* **Temperature:** In degree Celsius.
* **Humidity:** Relative humidity in %.
* **pH:** Soil pH value.
* **Rainfall:** In mm.

---
