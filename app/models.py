# Add any model classes for Flask-SQLAlchemy here
from . import db

class Posts(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer, primary_key=True) #, unique=True
    caption = db.Column(db.String(80))
    photo = db.Column(db.String(124))
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, caption, photo, user_id, created_at):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        self.created_at = created_at
        
    def __repr__(self):
        return '<posts %r>' % (self.user_id) 


class Likes(db.Model):
    __tablename__='likes'
    id = db.Column(db.Integer, primary_key=True) #, unique=True
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
   
    
    def __init__(self, post_id,user_id):
        self.post_id = post_id
        self.user_id = user_id
        
    def __repr__(self):
        return '<likes %r>' % (self.post_id)


class Follows(db.Model):
    __tablename__='follows'
    id = db.Column(db.Integer, primary_key=True) #, unique=True
    follower_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    
    def __init__(self, follower_id,user_id):
        self.follower_id = follower_id
        self.user_id = user_id
        
    def __repr__(self):
        return '<likes %r>' % (self.post_id)
    

class Users(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True) #, unique=True
    username = db.Column(db.String(80))
    password = db.Column(db.String(256))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    profile_photo = db.Column(db.String(80))
    joined_on = db.Column(db.DateTime, nullable=False)
   
    def __init__(self, username,password,firstname,lastname,email,location,biography,profile_photo,joined_on):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on

    def __repr__(self):
        return '<users %r>' % (self.username)

