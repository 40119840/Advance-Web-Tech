import sqlite
from sys import argv
from flask import Flask, request, render_template
from flask.ext.bcrypt import generate_password_hash

app = Flask(__name__)
db_location = 'var/data.db'

#database functions
def get_db():
    db = getattr(g, 'db',None )
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_ressource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        dn.commit


#routing
@app.route("/", methods={"GET","POST"})
def profile():
  return render_template('home.html')

@app.route("/login", methods={"GET","POST"})
def login():
  return render_template('login.html')


@app.route("/feed", methods={"GET","POST"})
def feed():
  return render_template('feed.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
