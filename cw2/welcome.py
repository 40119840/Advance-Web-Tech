from flask import Flask, redirect, url_for, abort, request, render_template, session, g, flash
import sqlite3
import ConfigParser
from flask.ext.wtf import Form
from wtforms import TextField
from contextlib import closing

#app create
app = Flask(__name__)
db_location = 'var/data.db'
#database functions


def get_db():
    db = getattr(g,'db',None)
    if db is None:
      db =sqlite3.connect(db_location)
      g.db = db
      db.row_factory = sqlite3.Row
      return db

@app.teardown_request
def teardown_request(exception):
  db = getattr(g,'db', None)
  if db is not None:
    db.close

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_ressource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit

#def query_db(query, arg=(), one=False):
#    db = get_db()
#    cur = db.execute(query,args)
#    rv = [dict((cur.description[idx][0], value) for idx, value in enumerate(row)) for row in cur.fetchall()]
#    return (rv[0] if rv else None) if one else rv

@app.route('/display')
def print_users():
    db = get_db()
    cur = db.execute('SELECT username,password FROM user ORDER BY id ASC')
    entries = [dict(username=row[0],password=row[1]) for row in cur.fetchall()]
    return render_template('displayUsers.html',entries=entries)



@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template ('createAccount.html')
    if request.method == 'POST':
      error = []
      form = request.form
      #query = 'SELECT * FROM user WHERE username = ?'
      #testUsername = query_db,(query, [request.form['username']])
      #if testUsername:
      #    error.append('please enter a diffrent username')
      if request.form['password'] != request.form["confirm_password"]:
          error.append("please enter same password")
      if not error:
          db = get_db()
          #insert in db
          db.cursor().execute('INSERT INTO user (username,password) values (?,?)',[request.form['username'],request.form['password']])
          db.commit()
          return render_template ('displayUsers.html')

#THIS IS NOT A GOOD VERSION / TEST 
@app.route("/discplay", methods={"GET","POST"})
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
  print "select thing working"
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
  return render_template('createaccount.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)


