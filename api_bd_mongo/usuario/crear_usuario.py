from flask_restful import Resource, request

from wtforms import Form, validators, StringField, PasswordField

class NewUserForm(Form):
    nombre = StringField('Usuario', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class NewUser(Resource):
    def post(self):
        form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400

        return 'ok', 200