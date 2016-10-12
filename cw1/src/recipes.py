from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Emma Reavley Cookbook"

@app.route("/home/")
def home():
    return "Start your adventure today"

@app.route("/page/")
def page():
    return "Title"

@app.route("/force404/")
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page requested", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
