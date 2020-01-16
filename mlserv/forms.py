from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

class ImageForm(FlaskForm):
    """Image form used for image submission to the server."""
    img = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], '.jpg, .jpeg and .png images only')])
    submit = SubmitField('Predict')