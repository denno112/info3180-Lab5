"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, jsonify, send_file, send_from_directory
import os
from app.models import Movies
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from .forms import MovieForm
from app import db
import json


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route("/api/v1/movies", methods=['GET','POST'])
def movies():
    form = MovieForm()
    if request.method == "GET":
        return test()
    # if request.method == "GET":
    #     data = Movies.query.all()
    #     print(data)
        # return jsonify({"data": data})
    if request.method == 'POST' and form.validate_on_submit():
        title = request.form['title']
        desc = request.form['desc']
        # poster = request.form['poster']

        f = form.poster.data
        filename = secure_filename(f.filename)
        img_url = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        f.save(img_url)

        movie = Movies(
            title=title,
            desc=desc,
            poster=filename
        )

        db.session.add(movie)
        db.session.commit()
        return jsonify(
            {
                "message": "Movie Successfully added",
                "title": str(title),
                "poster": str(filename),
                "description": str(desc)
            }
        )
    else:
        return jsonify({
            "errors": form_errors(form)
        })
    

def test():
    data = Movies.query.all()
    # print(json.dumps(data[0]))
    # for item in data:
    list = []
    # obj = {
    #     "title": data[0].title,
    # }
    for item in data:
        obj = {
            "title": item.title,
            "description": item.desc,
            "poster": "/api/v1/posters/" + item.poster
        }
        list.append(obj)

    # print(jsonify(list))
    return jsonify({"movies": list})
    
    # return jsonify({"movies":})
    # return jsonify({"test": data})  
@app.route("/api/v1/posters/<filename>", methods=['GET'])
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

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
    return render_template('404.html'), 404