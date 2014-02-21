from flask import Flask

app = Flask(__name__)
app.secret_key = 'chang3m3!'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'myemail@gmail.com'
app.config["MAIL_PASSWORD"] = 'testingpassword1233'

app.config["OPENID_PROVIDERS"] = [
          { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
          { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
          { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
          { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
          { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

from routes import mail
mail.init_app(app)

import intro_to_flask.routes
