import sqlite3
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
    
    app.config['log_file'] = config.get("logging","name")
    app.config['log_location'] = config.get("logging","location")

  except:
    print "Could not read configs from:", config_location
    
    
def logs(app):
  log_pathname = app.config['log_location'] + app.config['log_file']
  file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024*10,backupCount=1024)
  file_handler.setLevel(app.config['log_level'])
  formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s |\
  %(funcName)s | %(message)s")
  file_handler.setFormatter(formatter)
  app.logger.setLevel(app.config['log_level'])
  app.logger.addHandler(file_handler)    
    
    

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
