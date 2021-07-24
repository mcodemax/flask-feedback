"""Models for User"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

MAX_USERNAME_LEN = 20
MAX_NAME_LEN = 30
MAX_EMAIL_LEN = 50
MAX_NOTE_LEN = 5000
MAX_TITLE_LEN = 100

class User(db.Model):
    """Users."""

    __tablename__ = "users"

    def __repr__(self):
        return f"""<user id={self.id} password={self.password} email={self.email} first_name={self.first_name}
                last_name={self.last_name}>"""

    id = db.Column(db.Integer, # int not the same as SQL Integer, the ORM translates etween python and postgreSQL
                    primary_key=True,
                    autoincrement=True)
    
    username = db.Column(db.String(MAX_USERNAME_LEN),
                            nullable=False)
    
    password = db.Column(db.String(), #needs max len?
                            nullable=False)

    email = db.Column(db.String(MAX_EMAIL_LEN),  #maybe import email or use email from documentation?
                            nullable=False)

    first_name = db.Column(db.String(MAX_NAME_LEN),
                        nullable=False)


    last_name = db.Column(db.String(MAX_NAME_LEN),
                        nullable=False)
    
    #def function to salt/encrpyt password
    
    #def serialize_cupcake(self):
        # """serialize cupcakes"""
        
        # return {
        #     "id": self.id,
        #     "flavor": self.flavor,
        #     "size": self.size,
        #     "rating": self.rating,
        #     "image" : self.image
        # }

class Feedback(db.Model):
    """Feedback."""

    __tablename__ = "feedback"

    def __repr__(self):
        return f"""<feedback id={self.id} title={self.title} content={self.content} username={self.username}>"""


    id = db.Column(db.Integer, # int not the same as SQL Integer, the ORM translates etween python and postgreSQL
                    primary_key=True,
                    autoincrement=True)
    
    title = db.Column(db.String(MAX_TITLE_LEN),
                        nullable=False)

    content = db.Column(db.String(),
                        nullable=False)

    username = db.relationship("User", backref="feedback", cascade="all, delete-orphan")
    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete 
