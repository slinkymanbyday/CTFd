import os
import datetime
##### SERVER SETTINGS #####
SECRET_KEY = os.urandom(64)
SQLALCHEMY_DATABASE_URI = 'sqlite:///ctfd.db'
SESSION_TYPE = "filesystem"
SESSION_FILE_DIR = "/tmp/flask_session"
SESSION_COOKIE_HTTPONLY = True
PERMANENT_SESSION_LIFETIME = datetime.timedelta(7) # 7 days
HOST = "scoring.scurry"
UPLOAD_FOLDER = os.path.normpath('static/uploads')

##### EMAIL (Mailgun and non-Mailgun) #####

# The first address will be used as the from address of messages sent from CTFd
ADMINS = []

##### EMAIL (if not using Mailgun) #####
CTF_NAME = 'Scurry 2015'
MAIL_SERVER = ''
MAIL_PORT = 0
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
