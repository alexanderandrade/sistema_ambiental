from pymongo import MongoClient
from flask import Flask
from flask_restful import Resource, Api
from bson.json_util import dumps

class insert(Resource):
  def post(self,nombre,timestamp,medida):
    client = MongoClient('localhost',27017)
    db = client.test
    col=db.sensor
    try:
      col.insert(
        [
          { 'name': nombre, 'timestamp': timestamp, 'medida': medida},
        ]
      )
      return 'ok, insercion exitosa',400
    except:
      return 'error, fallo de ejecucion',200

class consultar(Resource):
  def get(self,nombre):
    client = MongoClient('localhost',27017)
    db = client.test
    col=db.sensor
    try:
      response=dumps(col.find({"name": nombre}))
      return response
    except:
      return 'error, fallo de ejecucion',200

