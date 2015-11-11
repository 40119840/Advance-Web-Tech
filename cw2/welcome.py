from sys import argv
from flask import Flask, request, render_template
app = Flask (__name__)

@app.route("/", methods={"GET","POST"})
def profile():
  return render_template('home.html')

@app.route("/login", methods={"GET","POST"})
def login():
  return render_template('login.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  
