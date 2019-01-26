from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    username = StringField('Usuario o Tendencia', validators=[DataRequired(), Length(min=2, max =50)])
    submit = SubmitField('Buscar')