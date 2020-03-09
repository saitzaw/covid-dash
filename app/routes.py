"""Routes for main flask application."""
from flask import Blueprint, render_template 
from flask import current_app as app 

main_blueprint = Blueprint('main_blueprint', __name__, 
                            template_folder='templates',
                            static_folder='static')

@main_blueprint.route('/')
def home_page(): 
    """Loading the Home page"""
    return render_template('index.html',title="COVID-19 DATA")