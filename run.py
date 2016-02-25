#! /usr/bin/env python

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from functions.functions import *

appdir = os.path.dirname(os.path.abspath(__file__))

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

@app.route('/')
def index():
    file_list = list_files(appdir)
    return render_template('index.html', file_list=file_list)

@app.route('/display_file/<filename>', methods=['GET', 'POST'])
def read_file(filename):
    file_list = list_files(appdir)
    text = get_file_from_list(appdir, filename)
    form = DataEntryForm(request.form)
    if form.validate_on_submit():
        highlight = form.name.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        title = form.title.data
        person_type = form.person_type.data
        comments = form.comments.data
        form_data=[highlight,filename,last_name,first_name,title,person_type,comments]
        write_line(form_data)
        flash('You successfully added %s, %s.' % (last_name, first_name), 'success')
        return render_template('index.html', filename=filename, text=text, file_list=file_list, form=form)
    return render_template('index.html', filename=filename, text=text, file_list=file_list, form=form)


app.secret_key='cardigan'
app.run(debug=True)
