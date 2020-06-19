"""Routes for main flask application."""
from flask import Blueprint, render_template, request 
from flask_security import login_required
from flask import current_app as app 

main_blueprint = Blueprint('main_blueprint', __name__, 
                            template_folder='templates',
                            static_folder='static')

@main_blueprint.route('/')
def home_page(): 
    """Loading the Home page"""
    return render_template('index.html',
                            title="COVID-19 DATA",
                            template='home-template',
                            body='COVID-19 DATA for global and local data visualization')

@main_blueprint.route('/local') 
def local_map(): 
    return render_template('map.html', template='home-template')

@main_blueprint.route('/register', methods=['POST','GET'])
def admin(): 
   return render_template('/login/register.html')

@main_blueprint.route('/profile')
@login_required
def profile(): 
    return render_template('/login/profile.html')