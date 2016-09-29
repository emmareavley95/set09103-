from flask import Flask, redirect, url_for
app = Flask(__name__)

#@app.route("/private")
#def private():
## test for user logged in failed
## so redirect to login URL
#  return redirect(url_for('login'))

#@app.route('/login')
#def login():
#  return "Now we would username &password"

#@app.route("/")
#def root():
#  return "The default, 'root' route"

@app.route("/")
def hello():
  return "Hello Napier from Emma!"

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested", 404

#@app.route("/goodbye/")
#def goodbye():
#  return "goodbye cruel world :("

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

