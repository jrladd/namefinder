#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, codecs, csv, os
from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Required


class DataEntryForm(Form):
    name = TextField('Highlighted Name')
    first_name = TextField('First Name', validators=[Required()])
    last_name = TextField('Last Name')
    title = TextField('Title')
    person_type = SelectField(u'Type', validators=[Required()], choices=[('author', 'Author'), ('dedicatee', 'Dedicatee'), ('other', 'Other')], default=('', 'Select Type'))
    comments = TextAreaField('Comments')
    submit = SubmitField('Submit')

#   Make these paths absolute.  It's easier that way.

def list_files(appdir):
    files = glob.glob(appdir+'/texts/*.txt')
    print appdir
    results = [f[-12:-4] for f in files]
    return results

def get_file_from_list(appdir, filename):
    files = glob.glob(appdir+'/texts/*.txt')
    for f in files:
        if f[-12:] == filename+'.txt':
            text = codecs.open(f, 'r', 'utf-8').readlines()
    return text

def write_line(form_data):
    with open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(form_data)



if __name__ == '__main__':

    results = get_ngrams_list_db()

    print 'results', results
    print 'len(results)', len(results)

    results = get_stanzas_for_quote(7)

    print 'results', results
    print 'len(results)', len(results)
