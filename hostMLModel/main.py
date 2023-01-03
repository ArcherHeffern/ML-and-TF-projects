from flask import Flask, request, Response, jsonify
from model import load_model

# TODO: Set up ssl

model = load_model() # make the model accessable to the entire program

app = Flask(__name__)

@app.route("/")
def index():
    return "Root"

@app.route("/predict", methods=['GET'])
def predict():
    # security?
    # must ensure: body is json, body contains celcius parameter, celcius is a float/int
    if request.headers.get('Content-Type') != 'application/json':
        return Response("Content type not application/json", 400)
    celcius = request.get_json().get('data')
    if celcius == None or float != type(celcius) != int:
        return Response("Did not have celcius parameter in body or was not a float/int", 400, mimetype='text/plain')
    else:
        result = model.predict([celcius])
        result = {"temperature": float(result[0][0])}
        return jsonify(result)
            

if __name__ == '__main__':
    app.run(debug=True)
