from flask import Flask

app = Flask(__name__)
app.secret_key = 'chang3m3!'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'myemail@gmail.com'
app.config["MAIL_PASSWORD"] = 'testingpassword1233'

from routes import mail
mail.init_app(app)

import intro_to_flask.routes
