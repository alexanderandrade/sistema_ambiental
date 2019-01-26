from flask import Flask
from flask_restful import Resource, Api
from usuario.crear_usuario import NewUser
from crud.conexion import insert, consultar

app= Flask(__name__)
api = Api(app)
api.add_resource(NewUser, '/api/v1/entrada')
api.add_resource(insert, '/api/v1/insertar/<nombre>_<timestamp>_<medida>')
api.add_resource(consultar, '/api/v1/consultar/<nombre>')

if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=5000)