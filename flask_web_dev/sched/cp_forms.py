from wtforms import Form, BooleanField, DateTimeField
from wtforms import TextAreaField, TextField
from wtforms.validators import Length, required

class AppointmentForm(Form):
    title = TextField('Title', [Length(max=255)])
    start = DateTimeField('Start', [required()])
    end = DateTime('End')
    allday = BooleanField('AllDay')
    location = TextField('Location', [Length(max=255)])
    description = TextArea('Description')


