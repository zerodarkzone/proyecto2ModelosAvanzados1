from lightgbm import LGBMRegressor
from flask import Flask
from flask import request
import pandas as pd
import numpy as np

import pickle
  
app = Flask(__name__)
reg_model = None
with open("notebook/LGBMRegressor3.pkl", "rb") as fim:
	reg_model = pickle.load(fim)
	
reg_model2 = None
with open("notebook/CatBoostRegressor.pkl", "rb") as fim:
	reg_model2 = pickle.load(fim)
  
@app.route("/", methods=['GET'])
def home_view():
    return "<h3>Request de Ejemplo:</h3><p>El Siguiente request corresponde a un Nissan Murano AWD modelo 2014 con un millaje de 31909 y matriculado en el estado de Maryland EEUU:</p><a href=""https://proyecto2-modelosa-vanzados1.herokuapp.com/predict?year=2014&mileage=31909&state=md&make=nissan&model=muranoawd"" target=""self"">https://proyecto2-modelosa-vanzados1.herokuapp.com/predict?year=2014&mileage=31909&state=md&make=nissan&model=muranoawd</a>"
		
@app.route("/predict", methods=['GET'])
def predict():
	try:
		year = int(request.args.get('year'))
		mileage = int(request.args.get('mileage'))
		state = request.args.get('state').upper()
		make = request.args.get('make').upper()
		model = request.args.get('model').upper()
		values = pd.DataFrame(np.array([year, mileage, state, make, model]).reshape(-1, 5), columns=["Year", "Mileage", "State", "Make", "Model"])
		values.loc[:,"Year"] = values["Year"].astype("float").astype("int64")
		values.loc[:,"Mileage"] = values["Mileage"].astype("float").astype("int64")
		values.loc[:,"State"] = values["State"].astype("category")
		values.loc[:,"Make"] = values["Make"].astype("category")
		values.loc[:,"Model"] = values["Model"].astype("category")
		cost1 = reg_model.predict(values)[0]
		cost2 = reg_model2.predict(values)[0]
		return {"cost": np.mean([cost1, cost2])}
	except Exception as e:
		print(e)
		return {"error": "Invalid parameters"}
		