from flask import Flask
from flask_restful import Resource, Api
import conexion_twitter as ct
import tendencia as tend 

app = Flask(__name__)
api_twitter = Api(app)

class Default(Resource):
    def get(self,nombre):
        return({"Bienvenido": nombre})

class Buscar(Resource):
    def get(self,nombre):
        persona = ct.twitter(nombre)
        return persona

class Tendencia(Resource):
    def get(self,palabra,cantidad,idioma):
        datos = tend.Tendencia()
        respuesta=datos.obtener_tendencia(palabra,cantidad,idioma)
        return respuesta



if __name__ == "__main__":
    api_twitter.add_resource(Default,'/<nombre>')
    api_twitter.add_resource(Buscar,'/consultar/<nombre>')
    api_twitter.add_resource(Tendencia,'/tendencia/<palabra>_<cantidad>_<idioma>')
    app.run(debug=True)
