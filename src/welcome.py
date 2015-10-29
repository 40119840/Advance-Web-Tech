from flask import Flask, request, render_template
app = Flask (__name__)

@app.route("/home/")
def home():
  return render_template('header.html')

@app.route("/home/players")
def players():
  return render_template('players.html')

@app.route('/home/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('Hello.html', user=user)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

