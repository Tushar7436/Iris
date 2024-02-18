from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('savedmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.get_json(force=True)
    # prediction = model.predict([data['features']])
    # return jsonify(prediction=prediction.tolist())
    data = [x for x in request.form.values()]
    prediction = model.predict(data)
    return render_template('index.html', prediction)

if __name__ == '__main__':
    app.run(debug=True)
