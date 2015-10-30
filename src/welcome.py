from sys import argv
from flask import Flask, request, render_template
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
  return render_template ('tow.html')

@app.route('/home/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('Hello.html', user=user)

@app.route("/search", methods={"GET","POST"})
def search():
    lol = []
    gogo = []
    html = ''
    empty = ''
    mem = []
    Data = open("static/data.txt", "r")
    txt  = myFile.reading()
    while txt:
        txt = myFile.readline{}
        if txt != empty:
          lol = txt.split("@")
          gogo =  lol[2]
          div = '''<div class="Entity">''' + gogo + '''</div>'''
          html = div + html
    Data.close()
    print html
    content = Markup(html)
    print content
    #return content
    return render_template('search.html',content=content)



if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

