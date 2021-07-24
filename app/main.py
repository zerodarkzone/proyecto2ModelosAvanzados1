from lightgbm import LGBMRegressor
from flask import Flask
from flask import request
import pandas as pd

import pickle
  
app = Flask(__name__)
model = None
with open("notebook/LGBMRegressor3.pkl", "rb") as fim:
	model = pickle.load(fim)
  
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
		cost = model.predict(pd.DataFrame(np.array([year, mileage, state, make, model])), columns=["Year", "Mileage", "State", "Make", "Model"])
		return {"cost": cost}
	except Exception as e:
		print(e)
		return {"error": "Invalid parameters"}
		