
from flask import Flask, url_for, abort
app = Flask(___name___)


@app.route('/static-exemple/img')
def static_exemple_img():
  start = '<img src="'
  url = url_for('static', filename='vmask.jpg')
  end = '">' 
  return start+url+end, 200

if _ _
