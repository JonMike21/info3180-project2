"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db , login_manager
from flask import render_template, request, jsonify, send_file,  redirect, url_for, flash, session, abort,send_from_directory
import os
from app.models import Posts,Likes,Follows,Users
from app.forms import UserForm,LoginForm, PostForm
from werkzeug.utils import secure_filename
import datetime
from flask_wtf.csrf import generate_csrf
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity



###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/register', methods=['POST'])
def register():
    form=UserForm()
    if form.validate_on_submit():
        username= form.username.data
        password= form.password.data
        firstname= form.firstname.data
        lastname= form.lastname.data
        email= form.email.data
        location= form.location.data
        biography= form.biography.data
        profile_photo_data= form.profile_photo.data
        profile_photo= secure_filename(profile_photo_data.filename)
        profile_photo_data.save(os.path.join(app.config['UPLOAD_FOLDER'],profile_photo))

        joined_on= datetime.datetime.now()
        #sets saves current time

        new_user=Users(username,password,firstname,lastname,email,location,biography,profile_photo,joined_on)
        #adds new user to db

        db.session.add(new_user)
        db.session.commit()
        #need to hash the password

        user={
            'message': 'User Successfully added',
            'username': username,
            'password': password,
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'location': location,
            'biography': biography,
            'profile_photo': profile_photo,
            'joined_on': joined_on
        }
        return jsonify(user)
    return jsonify(errors=form_errors(form))


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/v1/auth/login',methods=['POST'])
def login():
    form=LoginForm()
    
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        
        user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()
        if user is not None and check_password_hash(user.password, password):
            # Gets user id, load into session; flask login function
            login_user(user)
            response = {'result' :'Logged in successfully.', 
                            'id': user.id,
                            'username': user.username,
                            'firstname': user.firstname,
                            'lastname': user.lastname,
                            'email': user.email,
                            'location': user.location,
                            'biography': user.biography,
                            'profile_photo': user.profile_photo,
                            'joined_on': user.joined_on,
                            'token': create_access_token(identity=user.id),
                            }
            return jsonify(response),200
        else:
            return jsonify(result='Username or Password is incorrect.') 
    return jsonify(result=form_errors(form))



@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(Users).filter_by(id=id)).scalar()
    #gets current login user data from db


@app.route('/api/v1/auth/logout',methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify(message='You have Logged-Out Sucessfully')


@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST','GET'])
@jwt_required()
def addPosts(user_id):
    form=PostForm()
    p_list=[]

    current_user = get_jwt_identity()

    if current_user == user_id:

        if request.method == 'POST':
            
            if form.validate_on_submit():
                caption= form.caption.data
                photo_data= form.photo.data
                photo= secure_filename(photo_data.filename)
                photo_data.save(os.path.join(app.config['UPLOAD_FOLDER'],photo))

                created_at= datetime.datetime.now()

                post=Posts(caption,photo,user_id,created_at)

                db.session.add(post)
                db.session.commit() 

                post_n={
                    'message': 'Post Successfully added',
                    'caption': caption,
                    'photo': photo,
                    'created_at': created_at
                }
                return jsonify(post_n)
            return jsonify(errors=form_errors(form))
        
        if request.method == 'GET':
            if not user_id:
                response = {
                    'error': 'User not found'
                }
                return (response), 404

            idd=user_id
            u_posts = db.session.query(Posts).filter_by(user_id=idd).all()
            numposts = len(u_posts)
            for pos in u_posts:
                p_list.append({
                    'id': pos.id,
                    'caption': pos.caption,
                    'photo': url_for('getImage',filename=pos.photo),
                    'created_at': pos.created_at
                })
            
            user = db.session.query(Users).filter_by(id=user_id).first()
            user_info = {
                'id': user.id,
                'username': user.username,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'email': user.email,
                'location': user.location,
                'biography': user.biography,
                'profile_photo': url_for('getImage', filename=user.profile_photo),
                'joined_on': user.joined_on,
                'numposts': numposts
            }
            
            response_data = {
                'user_info': user_info
             }
            return jsonify(response_data)
    else:
        return redirect(url_for('login'))
        
@app.route('/api/users/<int:user_id>/follow', methods=['POST'])
@login_required
def follow(user_id):
    if current_user.is_authenticated:
        login_user_id = current_user.id #gets currently logged in user id
        follower_id=user_id #assuming the user_id is the target user
        follow=Follows(follower_id,login_user_id)

        db.session.add(follow)
        db.session.commit() 

        follow={
            'message': 'User was Successfully followed',
            'follower_id': follower_id,
            'user_id': login_user_id
        }
        return jsonify(follow)
    return jsonify(message='User not verified')
    
@app.route('/api/v1/posts', methods=['GET'])
def viewAllPosts():
    p_list=[]

    postss = db.session.execute(db.select(Posts)).scalars()

    for post in postss:
        p_list.append({
            'id': post.id,
            'caption': post.caption,
            'photo': url_for('getImage',filename=post.photo),
            'created_at': post.created_at
            })
    return jsonify(data=p_list)


@app.route('/api/v1/posts/<int:post_id>/like', methods=['POST'])
def likePosts(post_id):
    if current_user.is_authenticated:
        login_user_id = current_user.id #gets currently logged in user id
        like=Likes(post_id,login_user_id)

        db.session.add(like)
        db.session.commit() 

        follow={
            'message': 'Post was Successfully Liked',
            'post_id': post_id,
            'user_id': login_user_id
        }
        return jsonify(follow)

@app.route('/api/v1/photo/<filename>')
def getImage(filename):
    val=send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)
    return val
    


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,access-control-allow-origin')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response        
        

    





###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(errors=error)