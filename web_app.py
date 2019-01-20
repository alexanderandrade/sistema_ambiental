from flask import Flask
import requests

app= Flask(__name__)
@app.route('/consultar/<nombre>')
def consultar(nombre):
    info = requests.get('http://0.0.0.0:5000/consultar/'+nombre)
    return info.text

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)