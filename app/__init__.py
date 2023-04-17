from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS



app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)

#from app import models

db = SQLAlchemy(app)
migrate = Migrate(app, db)
cors = CORS(app)


from app import views


