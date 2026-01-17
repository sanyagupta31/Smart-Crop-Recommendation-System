from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Models load karo
dt_model = pickle.load(open('dt_crop_model.pkl', 'rb'))
rf_model = pickle.load(open('rf_crop_model.pkl', 'rb'))

crop_labels = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas', 'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate', 'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_crop', methods=['POST'])
def predict():
    try:
        # Form se data nikalna
        if request.form:
            data = request.form
        else:
            data = request.json
            
        input_data = np.array([[float(data['N']), float(data['P']), float(data['K']), 
                                float(data['temperature']), float(data['humidity']), 
                                float(data['ph']), float(data['rainfall'])]])
        
        probs_rf = rf_model.predict_proba(input_data)[0]
        prediction = crop_labels[np.argmax(probs_rf)].title()
        
        # Agar browser se request aayi hai toh HTML dikhao
        if request.form:
            return render_template('index.html', result=prediction)
        
        # Agar API request hai toh JSON bhejo
        return jsonify({"recommended_crop": prediction, "status": "Success"})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)