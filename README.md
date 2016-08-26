# The EEBO-TCP "Name Finder"

After some attempts at identifyng and collecting names in [EEBO-TCP](http://www.textcreationpartnership.org/tcp-eebo/) dedications with named-entity recognition, I decided to instead attempt to streamline the manual collection of names.

This simple web app, built on the [Flask microframework](http://flask.pocoo.org/), takes a series of plaintext files of dedications (derived from the EEBO-TCP xml), and serves them to a user who can add names to a csv file by highlighting them. This method still requires visually scanning each dedication, but makes the data entry and management a little easier and a lot quicker. I also used [Twitter bootstrap](http://getbootstrap.com/) to create a readable interface.

To try it out for yourself, simply download the files (or clone the repo), navigate to the newly-created directory on the command line, and run with `python run.py`.
