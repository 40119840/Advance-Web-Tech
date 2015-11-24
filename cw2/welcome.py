import sqlite3
from sys import argv
from flask import Flask, request, render_template, g, redirect, session
from contextlib import closing
import ConfigParser


app = Flask(__name__)
db_location = 'var/data.db'


#database functions
def get_db():
    db = getattr(g, 'db',None )
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

#def query_db(query, args=(), one=False):
#    db = get_db()
#    cur = db.execute(query, args)
#    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
#    return (rv[0] if rv else None) if one else rv    

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g,'db',None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit

def init(app):
  config = ConfigParser.ConfigParser()
  config_location = "etc/configuration.cfg"
  try: 
    config.read(config_location)

    app.config['debug'] = config.get("config","debug")
    app.config['ip_address'] = config.get("config","ip_address")
    app.config['port'] = config.get("config","port")
    app.config['url'] = config.get("config","url")

    app.config['database'] = config.get("config","database")
    app.config['secret_key'] = config.get("config","secret_key")
    app.config['username'] = config.get("config","username")
    app.config['password'] = config.get("config","password")
  except:
    print "Could not read configs from:", config_location




#routing
@app.route('/register', methods=['GET', 'POST'])
def createAccount():
    if request.method == 'POST':
        error = []
        form = request.form
        # Check if the username exists
        # ExistingUser = 'SELECT * FROM user WHERE username = ?'
        # DuplicateUser = query_db(ExistingUser, [request.form['username']])
        # if DuplicateUser:
        #     error.append("Sorry, this username is not available. Please choose another one")
        # Check if the passwords are identical
        if request.form['password'] != request.form['confirm_password']:
            error.append("Please enter the same password in both of the password fields")
        # Insert in the database if everything is ok
        if not error:
            # Insert
            db = get_db()
            db.cursor().execute('INSERT INTO users (username, password,) VALUES (?,?)', [request.form['username'], request.form['password']])
            db.commit()
            flash('You were successfully registered. Try to log in!')
            return render_template('login.html')
        return render_template('createAccount.html', form=form, error=error)
   # return render_template('createAccount.html')



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
