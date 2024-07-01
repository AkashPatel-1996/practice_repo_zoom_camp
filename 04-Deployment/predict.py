import pickle
import flask

from flask import Flask,  request , jsonify

with open('Models/lin_beg.bin', 'rb') as f_in:
    (dv,model)= pickle.load(f_in)

app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])

def predict_end_point():
    ride = request.get_json()
    features = prepare_features(ride)
    pred = predict(features)
    print(pred)
    result = {"duration": pred}
    return jsonify(result)


def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    return preds[0]

def prepare_features(ride):
    features = {}
    features["PULocationID"] = ride["PULocationID"]
    features["DOLocationID"] = ride["DOLocationID"]
    return features


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)