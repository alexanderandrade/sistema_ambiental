from flask import Flask, render_template, redirect, url_for
import requests
from forms import SearchForm
import unicodedata
import json
from credenciales import secret_key

app= Flask(__name__)
app.config['SECRET_KEY'] = secret_key

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('consulta_perfil', nombre=form.username.data))
    return render_template('busqueda.html', form=form)

@app.route('/home/<nombre>')
def consulta_perfil(nombre):
    info = requests.get('http://127.0.0.1:5000/consultar/'+nombre)
    info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    info = json.loads(info)
    return render_template('show.html', info=info)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)