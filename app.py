#from dotenv import load_dotenv
import os
from IPython import embed
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

#load_dotenv()

#
# APP
#

app = Flask(__name__)

#
# DB
#

try:
    DATABASE_URL = os.environ["DATABASE_URL"]
except KeyError as e:
    DATABASE_URL = "postgresql://localhost/my_flask_app"
print(DATABASE_URL)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # db.init_app(app)

def rollback_and_print(error):
    print("  --> ERROR %s" % (error._message))
    db.session.rollback() # to avoid sqlalchemy.exc.InvalidRequestError

#
# MODELS
#

class Robot(db.Model):
    __tablename__ = "robots"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True)

    def __init__(self, options):
        self.name = options["name"]
        self.description = options["description"]

    def __repr__(self):
        return '<Robot %r>' % self.name










#
# ROUTES
#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
