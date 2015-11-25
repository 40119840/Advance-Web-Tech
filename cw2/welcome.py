from flask import Flask, redirect, url_for, abort, request, render_template, session, g, flash
import sqlite3

app = Flask(__name__)
db_location = 'data.db'
#database functions

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
        db = sqlite3.connect(db_location)
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

@app.route("/test")
def finaly():
    print "finally"
    db = get_db()
    db.cursor().execute('insert into user VALUES ("2", "adam", "good at sql")')
    db.commit()

    page=[]
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM user ORDER BY password"
    for row in db.cursor().execute(sql):
         page.append('<li>')
         page.append(str(row))
         page.append('<li>')
    page.append('</ul></html>')
    return ''.join(page)


@app.route('/print')
def printi():
    db = get_db()
    cursor = db.cursor().execute('SELECT username,password FROM user')
    entries = [dict(username=row[0],password=row[1]) for row in cursor.fetchall()]
    print "working"
    return render_template('test_db.html',entries=entries)

@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
      db = get_db()
      db.execute('insert into user (username,password) values (?,?)',[request.form['username'],request.form['password']
      db.commit()
      flash('new entry added')
      return render_template('createAccount.html')

#Routing
@app.route("/display", methods={"GET","POST"})
def display():
  print "running 1"
  db = get_db()
  print "caca 2"
  db.cursor().execute('INSERT INTO user (username, password) VALUES ("adaeem", "daphne")')
  print "lala 3"
  db.commit()
  print "sasa 4"
  reader()
  print "5"

  page = []
  page.append('<html><ul>')
  print "html start"
  sql = "SELECT rowid, * FROM user ORDER BY username"
  print "selesct thing working"
  for row in db.cursor().execute(sql):
      page.append('<li>')
      page.append(str(row))
      page.append('</li>')
  page.append('</ul></html>')
  print "end html"
  return  ''.join(page)

#@app.route('/register', methods=['GET', 'POST'])
#def createAccount():
#    if request.method == 'POST':
#      db = get_db()
#      db.cursor().execute('INSERT INTO user (username, password) VALUES (?,?)',[request.form['username'], request.form['password']])
#      db.commit()
#      flash('You were successfully registered. Try to log in!')
#      return render_template('createAccount.html', form=form, error=error)
#    return render_template('createAccount.html')



@app.route("/", methods={"GET","POST"})
def profile():
  return render_template('test_db.html')

@app.route("/login", methods={"GET","POST"})
def login():
  return render_template('login.html')


@app.route("/feed", methods={"GET","POST"})
def feed():
  return render_template('feed.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
