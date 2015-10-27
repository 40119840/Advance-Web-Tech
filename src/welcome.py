from flask import Flask, request
app = Flask (__name__)

@app.route("/home/")
def home():
  page='''
  <html>
    <body>
      <title>
        adam s movies
      </title>
      <p>Hello World</p>
    </body>
  </html>
  '''
  return page

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

