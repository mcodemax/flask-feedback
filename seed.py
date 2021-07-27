"""Seed file for Users"""

from models import User, Feedback, db
from app import app

def add_relation_tag(rel_to_append, tag_lst):
    
    for tag in tag_lst:
        rel_to_append.tags.append(tag)

    db.session.commit()


# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Feedback.query.delete()


# Add Users
user1 = User.register(username='Fname1', password="passy", email='Genny@hotmail.com', first_name="Tom", last_name = "Fiddle")

# Add new objects to session, so they'll persist
db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)
# db.session.add(user4)

# Commit--otherwise, this never gets saved!
db.session.commit()

feedback1 = Feedback(title='Cool', content='The place was coolio', username='Fname1')
feedback2 = Feedback(title='Unlit', content='The place was TRASH', username='Fname1')

db.session.add_all([feedback1, feedback2])
db.session.commit()