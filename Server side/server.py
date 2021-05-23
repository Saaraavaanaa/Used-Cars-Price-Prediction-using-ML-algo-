from flask import Flask, request, jsonify,render_template
from gevent.pywsgi import WSGIServer
from flask_cors import CORS, cross_origin

import subserver

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template("index.html")


# Load the location in the  Html 
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': subserver.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


#Load the names in the Htmal
@app.route('/get_car_names', methods=['GET'])
def get_car_names():
    response = jsonify({
        'name': subserver.get_car_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#load the Transmission in the Html

@app.route('/get_car_Transmission', methods=['GET'])
def get_car_Transmission():
    response = jsonify({
        'transmission': subserver.get_car_Transmission()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#Load the Fuel Type in the Html

@app.route('/get_car_Fuel_Type', methods=['GET'])
def get_car_Fuel_Type():
    response = jsonify({
        'fuel_type': subserver.get_car_Fuel_Type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

#Load the Owner_Type in the Html

@app.route('/get_car_Owner_Type', methods=['GET'])
def get_car_Owner_Type():
    response = jsonify({
        'Owner_Type': subserver.get_car_Owner_Type()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


#price Pridiction Code


@app.route('/predict_price', methods=['POST'])
def predict_price():

    km = float(request.form['kilo'])
    milg = float(request.form['mille'])
    egie= float(request.form['engine'])
    po = float(request.form['power'])
    se = int(request.form['seats'])
    year = int(request.form['year'])
    CName = request.form['name']
    Cloc = request.form['location']
    f_t = request.form['fuel']
    trans = request.form['Trans']
    o_t = request.form['owner']
    

    response = jsonify({
        'estimated_price': subserver.predict_price(CName,Cloc,year,km,f_t,trans,o_t,milg,egie,po,se)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

    

# server Run Code

if __name__ == "__main__":
    print("Starting Python Flask Server For Used Cars Price Prediction...")
    subserver.load_saved_pickles()
    # app.run(debug=True)

    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()