from flask import Flask
import requests

app= Flask(__name__)
@app.route('/home/<nombre>')
def home(nombre):
    info = requests.get('http://0.0.0.0:5000/'+nombre)
    return info.text

@app.route('/consultar/<nombre>')
def consultar(nombre):
    perfil= requests.get('http://127.0.0.1:5000/consultar/'+nombre)
    return perfil.text

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)