from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField

class ContactForm(Form):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")