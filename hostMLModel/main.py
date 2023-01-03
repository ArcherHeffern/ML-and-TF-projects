from flask import Flask, request, Response
from model import load_model

# TODO: Set up ssl

model = load_model() # make the model accessable to the entire program

app = Flask(__name__)

@app.route("/")
def index():
    return "Root"

@app.route("/predict", methods=['GET'])
def predict():
    if request.headers.get('Content-Type') == 'application/json':
        celcius = request.get_json().get('data')
        if celcius == None:
            print(celcius)
            result = model.predict([celcius])
            return Response({'temperature':result[0]}, 200, mimetype='text/plain')
        else:
            return Response("Did not have celcius parameter in body", 400, mimetype='text/plain')
    else:
        return Response("Content type not application/json", 400)

if __name__ == '__main__':
    app.run(debug=True)
