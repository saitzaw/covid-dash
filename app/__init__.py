#from .views import app
from flask import Flask 

def create_app(): 
    """ For the core application """ 

    app = Flask(__name__,instance_relative_config=False) 
    app.config.from_object('config.Config')
    with app.app_context(): 
        from app import routes 
        app.register_blueprint(routes.main_blueprint)

        from app.dash_global.views import global_dash 
        app = global_dash(app) 
        
        return app
