from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
class teams(FlaskForm):
    BlueSide = StringField('Blue Side', validators=[DataRequired()])
    RedSide = StringField('Red Side', validators=[DataRequired()])
    submit = SubmitField('Submit')
