from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class FileUploadForm(FlaskForm):
    file = FileField('파일을 업로드하세요.', validators=[DataRequired()])
    submit = SubmitField('업로드')