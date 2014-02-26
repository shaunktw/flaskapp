from flask import render_template, request, flash, redirect
from forms import ContactForm, LoginForm
from intro_to_flask import app
from flask.ext.mail import Message, Mail

mail = Mail()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required.')
			return render_template('contact.html', form = form)
		else:
			msg = Message(form.subject.data, sender='myemail@gmail.com', recipients=['mysecondemail@gmail.com'])
			msg.body = """From: %s <%s> %s """ % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return render_template('contact.html', form = form)
	elif request.method == 'GET':
		return render_template('contact.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
    	return redirect('/')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])  