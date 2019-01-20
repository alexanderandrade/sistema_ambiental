from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api_twitter = Api(app)

class Consultar(Resource):
    def get(self,nombre):
        return({"Hello": nombre})

if __name__ == "__main__":
    api_twitter.add_resource(Consultar,'/consultar/<nombre>')
    app.run(debug=True)
