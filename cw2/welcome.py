from flask import Flask, redirect, url_for, abort, request, render_template, session, g, flash
import sqlite3
app = Flask(__name__)
#database functions
#def query_db(query, args=(), one=False):
#    db = get_db()
#    cur = db.execute(query, args)
#    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
#    return (rv[0] if rv else None) if one else rv    


#def init(app):
#  config = ConfigParser.ConfigParser()
#  config_location = "etc/configuration.cfg"
#  try:
#    config.read(config_location)
#
#    app.config['debug'] = config.get("config","debug")
#    app.config['ip_address'] = config.get("config","ip_address")
#    app.config['port'] = config.get("config","port")
#    app.config['url'] = config.get("config","url")
#
#    app.config['database'] = config.get("config","database")
#    app.config['secret_key'] = config.get("config","secret_key")
#    app.config['username'] = config.get("config","username")
#    app.config['password'] = config.get("config","password")
#  except:
#    print "Could not read configs from:", config_location

#def connect_db():
#  init(app)
#  connect = sqlite3.connect(app.config['database'])
#  connect.row_factory = sqlite3.Row
#  return connect

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            print f
            db.cursor().executescript(f.read())
        db.commit()
        finaly()
        reader()

def get_db():
    print "getDB1"
    db = getattr(g, 'db', None)
    print "getDB2"
    if db is None:
        print "getDB3"
        db = sqlite3.connect('lol.db')
        db = db
    print "getDB4"
    print db
    return db

def reader():
    page = []
    db = get_db()
    sql = "SELECT id, * FROM user"
    for row in db.cursor().execute(sql):
        page.append(str(row))
    print page

def finaly():
    print "finaly"
    db = get_db()
    db.cursor().execute('insert into user values ("1", "adam", "good at sql")')
    db.commit()
#@app.before_request
#def before_request():
#  g.db = connect_db()

#@app.teardown_request
#def teardown_request(exception):
#  db = getattr(g,'db', None)
#  if db is not None:
#    db.close()

#routing
#@app.route('/register', methods=['GET', 'POST'])
#def createAccount():
#    if request.method == 'POST':
#        error = []
#        form = request.form
        # Check if the username exists
        # ExistingUser = 'SELECT * FROM user WHERE username = ?'
        # DuplicateUser = query_db(ExistingUser, [request.form['username']])
        # if DuplicateUser:
        #     error.append("Sorry, this username is not available. Please choose another one")
        # Check if the passwords are identical
#        if request.form['password'] != request.form['confirm_password']:
#            error.append("Please enter the same password in both of the password fields")
        # Insert in the database if everything is ok
#        if not error:
            # Insert
#            db = get_db()
#            db.cursor().execute('INSERT INTO users (username, password,) VALUES (?,?)', [request.form['username'], request.form['password']])
#            db.commit()
#            flash('You were successfully registered. Try to log in!')
#            return render_template('login.html')
#        return render_template('createAccount.html', form=form, error=error)
   # return render_template('createAccount.html')



#@app.route("/", methods={"GET","POST"})
#def profile():
#  return render_template('home.html')
#
#@app.route("/login", methods={"GET","POST"})
#def login():
#  return render_template('login.html')
#
#
#@app.route("/feed", methods={"GET","POST"})
#def feed():
#  return render_template('feed.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0')
