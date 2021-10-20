import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY']='mysecretkey'

##################################
########DATABASE##################
##################################

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

##################################
######LOGIN CONFIGS###############
##################################

login_manager=LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'


###################################
#########BLUEPRINTS################
###################################

from mnc_blog.core.views import core
app.register_blueprint(core)

from mnc_blog.error_pages.handler import error_pages
app.register_blueprint(error_pages)

from mnc_blog.users.views import users
app.register_blueprint(users)

from mnc_blog.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)