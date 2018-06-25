"""
The flask application package.
"""

# third-party imports
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


# local imports
from config import app_config

# db variable initialization

db=SQLAlchemy()
login_manager=LoginManager()





#def create_app(config_name):
#    app=Flask(__name__,instance_relative_config=True)
#    app.config.from_object(app_config[config_name])
#    app.config.from_pyfile('config.py')

#    db.init_app(app)
#    app=app
#    import myWeb.views

#    return app


app=Flask(__name__,instance_relative_config=True)
#config_name= os.getenv('FLASK_CONFIGURATION', 'default')
#config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')

Bootstrap(app)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_message="You must be logged in to access this page"
login_manager.login_view="auth.login"
migrate=Migrate(app,db)


from myWeb import models

# Import and Register Blueprint 
from .admin import admin
from .home import home
from .auth import auth

app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(home)
app.register_blueprint(auth)

# Custom Error Pages

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500




import myWeb.views




