"""Flask Feedback App."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Feedback
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from forms import AddLoginForm, AddUserForm


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
        
        if User.query.filter_by(username=data['username']).first():
            flash('User already exists')
            return redirect('/register')
        else:
            user = User.register(**data)
    
            db.session.add(user)
            db.session.commit()

            session['username'] = user.username

            
            return redirect(f"/users/{user.username}")

             # try:
            #     user = User.register(**data)
            # except:
            #     flash('User already exists')
            #     return redirect('/register')
    else:
        
        return render_template("add_user.html", form=form)

@app.route('/users/<username>')
def logged_in_user_info(username):
    """You get here if you're authenticated"""
    #protect this route w/validation
    #get current user
    if(session.get('username', None) == username): #makes sure only logged in user can see own info
        flash('You made it')
        user = User.query.filter_by(username=session['username']).first()
        return render_template('loggedinuser_info.html', user=user)
    else:
        flash("You aren't allowed to be here")
        return redirect('/')

@app.route('/login', methods=["GET", "POST"])
def login():
    
    form = AddLoginForm()
    
    if form.validate_on_submit():
        data = {field: val for field, val in form.data.items() if field != "csrf_token"}
        #stacked overflow:iterating over form fields in flask
        username = data['username']
        pwd = data  ['password']
        if(User.authenticate(username, pwd)):
            session['username'] = username
            return redirect(f"/users/{username}")
        else:
            flash('Login Failed; Try again!')
            return render_template("login.html", form=form)    
      
        
    else:
        
        return render_template("login.html", form=form)
    

# @app.route('users/<username>')
# def 

@app.route('/logout')
def logout():

    #session.pop('username', None)
    session.clear()

    return redirect("/")