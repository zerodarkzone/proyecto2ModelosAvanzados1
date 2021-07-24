
from flask import Flask
  
app = Flask(__name__)
  
@app.route("/", methods=['GET'])
def home_view():
    return "<h1>Hello world</h1>"
		
@app.route("/predict", methods=['GET'])
def predict():
	try:
		year = int(request.args.get('year'))
		mileage = int(request.args.get('mileage'))
		state = request.args.get('state')
		make = request.args.get('make')
		model = request.args.get('model')
		return {"cost": 25000}
	except Exception as e:
		return {"error": "Invalid parameters"}
		