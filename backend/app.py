from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = pickle.load(open('model/model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def get_data():
    data = {
        "message": "API is Running"
    }
    return jsonify(data)

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        data = request.get_json
        print("Received data:", data)  # Add this line for debugging
        if data is None:
            return jsonify({'error': 'Empty JSON payload'})
        dict={'Year':[1],'Present_Price':[2],'Kms_Driven':[3],'Fuel_Type':[4],'Seller_Type':[5],'Transmission':[6],'Owner':[7]}
        #query_df = pd.DataFrame(dict)
        query_df = pd.DataFrame(dict)
        print("Query DataFrame:", query_df)  # Add this line for debugging

        prediction = model.predict(query_df)
        #return jsonify(prediction)
        return jsonify({'Prediction': list(prediction)})
    except Exception as e:
        print("Error:", str(e))  # Add this line for debugging
        return jsonify({'error': str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=5001)
