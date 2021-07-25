"""Flask Feedback App."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Feedback
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from forms import AddUserForm


app = Flask(__name__)
CORS(app) #https://flask-cors.readthedocs.io/en/latest/
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5433/feedback' 
#@ people looking at this code; you may need to change on your own computer for code to work

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True #prints in ipython the queries being run

app.config["SECRET_KEY"] = "maxcode1"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

@app.route('/')
def show_title_get():

    

    return redirect("/register")

  
  
  
@app.route('/register', methods=["GET", "POST"])
def add_user_form():

    form = AddUserForm()

    if form.validate_on_submit():
        data = {field: val for field, val in form.data.items() if field != "csrf_token"}
        #stacked overflow:iterating over form fields in flask
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    else:
        
        return render_template("add_user.html", form=form)
