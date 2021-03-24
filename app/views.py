"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash 


from app.forms import PropertyForm
from app.models import Property

from werkzeug.utils import secure_filename
import os
import psycopg2

#Database Connection
import psycopg2
def connect_db():
    return psycopg2.connect(host="localhost", database="mydb", user="someuser", password="somepass")
 
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/property/', methods=['GET', 'POST'])
def new_property():
    # Loads up the form
    property_form = PropertyForm()

    # Checks for method type and validatation
    if request.method == 'POST':
        if property_form.validate_on_submit():

            # Collect the data from the form
            p_title = property_form.p_title.data
            description = property_form.p_description.data
            rooms = property_form.rooms.data
            bathrooms = property_form.bathrooms.data
            price = property_form.price.data
            p_type = property_form.p_type.data
            location = property_form.location.data

            photo = property_form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Create a Property object
            property = Property(p_title, description, rooms,
                                bathrooms, price, p_type, location, photo)
            db.session.add(property)
            db.session.commit()

            # Redirects user to the Properties page
            flash('New Property Added Successfully!', 'success')
            return redirect(url_for('all_properties'))
    else:
        flash_errors(property_form)

    return render_template('property.html', form=property_form)


@app.route('/properties/')
def all_properties():

    # Connect to the database
    db = connect_db()
    cur = db.cursor()

    cur.executes('SELECT * FROM Properties')
    properties = cur.fetchall()

    return render_template('properties.html', properties=properties)


@app.route('/property/<propertyid>')
def specific_property(property_id):
    property_id = int(property_id)

    # Locates the Property with the matching ID
    property = Property.query.filter_by(id=property_id).first()

    return render_template('property.html', property=property)





# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
