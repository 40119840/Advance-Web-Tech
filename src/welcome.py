from sys import argv 
from flask import Flask, request, render_template, Markup
app = Flask (__name__)

@app.route("/home/", methods={"GET","POST"})
def home():
    pick = []
    html = ''
    empty = ''
    x = 0
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    for txt in range(0,6):
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="http://localhost:5000/''' + pick[0] + '''">''' + pick[1] + '''</a></li>'''
          html = html + div
    Data.close()
    LAPlayers = Markup(html)
    return render_template('home.html',LAPlayers=LAPlayers)

@app.route("/home/players")
def player():
  return render_template('players.html')

@app.route("/home/tow")
def tow():
  return render_template ('tow.html',input=input)

@app.route('/home/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('Hello.html', user=user)

@app.route('/club/<token>') 
def club(token=None):
   lala = {'token' : token}
   #Data = open("static/data.txt", "r")
   #txt = Data.readline()
   if '3' in open("static/data.txt").read():
      print "True"


@app.route("/players", methods={"GET","POST"})
def players():
    pick = []
    html = ''
    empty = ''
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    while txt:
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="http://localhost:5000/''' + pick[0] + '''">''' + pick[1] + '''</a></li>'''
          html = html + div
    Data.close()
    input = Markup(html)
    return render_template('players.html',input=input)


@app.route("/clubs", methods={"GET","POST"})
def clubs():
    pick = []
    html = ''
    empty = ''
    x = 0
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    while txt:
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="http://localhost:5000/''' + pick[0] + '''">''' + pick[2] + '''</a></li>'''
          html = html + div
    Data.close()
    input = Markup(html)
    return render_template('clubs.html',input=input)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
