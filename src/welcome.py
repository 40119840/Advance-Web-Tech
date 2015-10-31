from sys import argv 
from flask import Flask, request, render_template, Markup
app = Flask (__name__)

@app.route("/home/")
def home():
  return render_template('home.html')

@app.route("/home/players")
def players():
  return render_template('players.html')

@app.route("/home/clubs")
def clubs():
   return render_template('clubs.html')

@app.route("/home/tow")
def tow():
  return render_template ('tow.html',input=input)

@app.route('/home/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('Hello.html', user=user)

@app.route("/players", methods={"GET","POST"})
def search():
    pick = []
    html = ''
    empty = ''
    Data = open("static/data.txt", "r")
    txt  = Data.readline()
    while txt:
        txt = Data.readline()
        if txt != empty:
          pick = txt.split("@")
          div = '''<li><a href="">''' + pick[1] + '''</a></li>'''
          html = html + div
    Data.close()
    input = Markup(html)
    return render_template('players.html',input=input)


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
