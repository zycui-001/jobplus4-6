from flask import Blueprint, render_template
from jobplus.forms import RegisterForm, LoginForm

front = Blueprint('front', __name__)

@front.route('/')
def index():
	return render_template('index.html')

@front.route('/register')
def register():
	form = RegisterForm()
	return render_template('register.html', form=form)

@front.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', form=form)