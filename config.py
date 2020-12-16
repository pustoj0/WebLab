import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'mysecret'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') # data.sqlite => site.db
SQLALCHEMY_TRACK_MODIFICATIONS = False
